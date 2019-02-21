const tf = require('@tensorflow/tfjs');
require('@tensorflow/tfjs-node');

let a = tf.scalar(2);
let b = tf.scalar(3);

console.log('a: '+a.dataSync()[0]+', b: '+b.dataSync()[0]);
