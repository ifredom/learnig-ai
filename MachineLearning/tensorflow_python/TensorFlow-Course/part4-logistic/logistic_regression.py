import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import tempfile
import urllib
import pandas as pd
import os
from tensorflow.examples.tutorials.mnist import input_data


old_v = tf.logging.get_verbosity()
tf.logging.set_verbosity(tf.logging.ERROR)

######################################
######### Necessary flags ############
######################################

max_num_checkpoint = 10
num_classes = 2
batch_size = 512
num_epochs = 10

##################################
######## 训练比率标志 #############
##################################

initial_learning_rate = 0.001
learning_rate_decay_factor = 0.95
num_epochs_per_decay = 1

#########################################
########## 状态标志 #################
#########################################

is_training = False
fine_tuning = False
online_test = True
allow_soft_placement = True
log_device_placement = False


# 载入MNIST数据集，如果指定地址下没有下载好的数据，那么TensorFlow会自动在网站上下载数据
# 默认情况下，reshape=True，表示提取特征向量，但我们将其设置为false以获得原始图像
mnist = input_data.read_data_sets("MNIST_data/", reshape=True, one_hot=False)


########################
### 数据处理 ####
########################
# 获取数据并将其储存在 data 字典上。
data = {}

data['train/image'] = mnist.train.images
data['train/label'] = mnist.train.labels
data['test/image'] = mnist.test.images
data['test/label'] = mnist.test.labels

# 只获取数据中标签为零和标签为一的数据用于学习训练。
def extract_samples_Fn(data):
    index_list = []
    for sample_index in range(data.shape[0]):
        label = data[sample_index]
        if label == 1 or label == 0:
            index_list.append(sample_index)
    return index_list


index_list_train = extract_samples_Fn(data['train/label'])
index_list_test = extract_samples_Fn(data['test/label'])

# 重组数据结构
data['train/image'] = mnist.train.images[index_list_train]
data['train/label'] = mnist.train.labels[index_list_train]

# 重组数据结构
data['test/image'] = mnist.test.images[index_list_test]
data['test/label'] = mnist.test.labels[index_list_test]

# 二元训练
dimensionality_train = data['train/image'].shape

# 形状
num_train_samples = dimensionality_train[0]  # num_train_samples ；11623
num_features = dimensionality_train[1]  # num_features：784

###############################################
########### 定义图  ############
###############################################
graph = tf.Graph()
with graph.as_default():
    ########### 特征 ############

    # 全局步长
    global_step = tf.Variable(0, name="global_step", trainable=False)

    # 制定学习比率策略
    decay_steps = int(num_train_samples / batch_size *
                      num_epochs_per_decay)
    learning_rate = tf.train.exponential_decay(initial_learning_rate,
                                               global_step,
                                               decay_steps,
                                               learning_rate_decay_factor,
                                               staircase=True,
                                               name='exponential_decay_learning_rate')
    ########### 定义占位符 ############
    image_place = tf.placeholder(tf.float32, shape=(
        [None, num_features]), name='image')
    label_place = tf.placeholder(tf.int32, shape=([None, ]), name='gt')
    label_one_hot = tf.one_hot(label_place, depth=num_classes, axis=-1)
    dropout_param = tf.placeholder(tf.float32)

    ##################################################
    ########### Model + Loss + Accuracy ##############
    ##################################################
    # A simple fully connected with two class and a softmax is equivalent to Logistic Regression.
    logits = tf.contrib.layers.fully_connected(
        inputs=image_place, num_outputs=num_classes, scope='fc')

    # Define loss
    with tf.name_scope('loss'):
        loss_tensor = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(
            logits=logits, labels=label_one_hot))

    # Accuracy
    # Evaluate the model
    prediction_correct = tf.equal(
        tf.argmax(logits, 1), tf.argmax(label_one_hot, 1))

    # Accuracy calculation
    accuracy = tf.reduce_mean(tf.cast(prediction_correct, tf.float32))

    #############################################
    ########### training operation ##############
    #############################################

    # Define optimizer by its default values
    optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate)

    # 'train_op' is a operation that is run for gradient update on parameters.
    # Each execution of 'train_op' is a training step.
    # By passing 'global_step' to the optimizer, each time that the 'train_op' is run, Tensorflow
    # update the 'global_step' and increment it by one!

    # gradient update.
    with tf.name_scope('train_op'):
        gradients_and_variables = optimizer.compute_gradients(loss_tensor)
        train_op = optimizer.apply_gradients(
            gradients_and_variables, global_step=global_step)

    ############################################
    ############ Run the Session ###############
    ############################################
    session_conf = tf.ConfigProto(
        allow_soft_placement=allow_soft_placement,
        log_device_placement=log_device_placement)
    sess = tf.Session(graph=graph, config=session_conf)

    with sess.as_default():

        # The saver op.
        saver = tf.train.Saver()

        # Initialize all variables
        sess.run(tf.global_variables_initializer())

        # The prefix for checkpoint files
        checkpoint_prefix = 'model'

        # If fie-tuning flag in 'True' the model will be restored.
        if fine_tuning:
            saver.restore(sess, os.path.join(
                checkpoint_path, checkpoint_prefix))
            print("Model restored for fine-tuning...")

        ###################################################################
        ########## Run the training and loop over the batches #############
        ###################################################################

        # go through the batches
        test_accuracy = 0
        for epoch in range(num_epochs):
            total_batch_training = int(
                data['train/image'].shape[0] / batch_size)

            # go through the batches
            for batch_num in range(total_batch_training):
                #################################################
                ########## Get the training batches #############
                #################################################

                start_idx = batch_num * batch_size
                end_idx = (batch_num + 1) * batch_size

                # Fit training using batch data
                train_batch_data, train_batch_label = data['train/image'][start_idx:end_idx], data['train/label'][
                    start_idx:end_idx]

                ########################################
                ########## Run the session #############
                ########################################

                # Run optimization op (backprop) and Calculate batch loss and accuracy
                # When the tensor tensors['global_step'] is evaluated, it will be incremented by one.
                batch_loss, _, training_step = sess.run(
                    [loss_tensor, train_op,
                     global_step],
                    feed_dict={image_place: train_batch_data,
                               label_place: train_batch_label,
                               dropout_param: 0.5})

                ########################################
                ########## Write summaries #############
                ########################################

                #################################################
                ########## Plot the progressive bar #############
                #################################################

            print("Epoch " + str(epoch + 1) + ", Training Loss= " +
                  "{:.5f}".format(batch_loss))

        ############################################################################
        ########## Run the session for pur evaluation on the test data #############
        ############################################################################

        # Evaluation of the model
        test_accuracy = 100 * sess.run(accuracy, feed_dict={
            image_place: data['test/image'],
            label_place: data['test/label'],
            dropout_param: 1.})

        print("Final Test Accuracy is %% %.2f" % test_accuracy)
