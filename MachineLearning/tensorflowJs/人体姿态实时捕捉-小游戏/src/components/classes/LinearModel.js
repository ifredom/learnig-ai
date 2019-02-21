import * as tf from '@tensorflow/tfjs';

export default class LinearModel {
  async trainModel(xs, ys){
    const layers = tf.layers.dense({  // layers图层
      units: 1,  // 空间的维数
      inputShape: [1],  // 参数个数，一个
    });
    const lossAndOptimizer = {
      loss: 'meanSquaredError',
      optimizer: 'sgd', // 随机梯度下降
    };

    this.linearModel = tf.sequential(); // 构造一个模型，
    this.linearModel.add(layers);
    this.linearModel.compile(lossAndOptimizer);

    await this.linearModel.fit(
      tf.tensor1d(xs),
      tf.tensor1d(ys),
    );
  }

  predict(value){
    return Array.from(
      this.linearModel
      .predict(tf.tensor2d([value], [1, 1]))
      .dataSync()
    )
  }
}
