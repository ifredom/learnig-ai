<template>
  <div class="page">
    <h2>使用tensoleflow.js线性模型训练。参考：https://juejin.im/post/5b971b295188255c581a8ff0</h2>

    <div>
      <input
        type="text"
        v-model.number="form.x"
        placeholder="输入X"
      >
      <input
        type="text"
        v-model.number="form.y"
        placeholder="输入Y"
      >
    </div>

    <div> <button @click="add">新增一条</button> <span>tips：至少输入3条数据后，再进行训练</span></div>
    <div class="container-border">
      <h4>已输入数据：</h4>
      <ul>
        <li
          v-for="(item,index) in trainData"
          :key="item+index"
        >{{`第${index}组. X:${item.x} Y:${item.y}`}}</li>
      </ul>
    </div>

    <div><button
        @click="train"
        v-if="trainData.length>=3"
      >开始训练</button><span>{{message.trainMsg}}</span></div>

    <div class="container-border">
      <h4>预测：根据已输入的几组数据对模型进行训练。<br />验证：输入X值，开始预测Y的值</h4>
      <input
        type="text"
        v-model.number="form.predictionX"
        placeholder="输入条件X值"
      >
      <button @click="predict">预测</button>
      <div>预测Y的值为：<span>{{form.predictionY}}</span></div>
    </div>

    <div class="fish" :style="fishStyle">fish</div>
  </div>
</template>

<script>
import LinearModel from "@/components/classes/LinearModel";

export default {
  data() {
    return {
      form: {
        x: "",
        y: "",
        predictionX: "",
        predictionY: ""
      },
      linearModel: new LinearModel(),
      trainData: [],
      message: {
        trainMsg: ""
      },
      timeout: "",
      fishStyle:{
        left:0,
        top:0
      }
    };
  },
  mounted() {
    this.initCapture();
  },
  methods: {
    initCapture() {
      var that = this
      let justan = 20
      this.timeout = setTimeout(function() {
        that.$nextTick(()=>{
        that.fishStyle ={
          left: 30+'px',
          top: 30+'px'
        }

        console.log(that.fishStyle);
        })


      }, 1000);
    },
    add() {
      this.trainData.push(JSON.parse(JSON.stringify(this.form)));

      this.form.x = "";
      this.form.y = "";
    },
    train() {
      const xs = this.trainData.map(data => data.x);
      const ys = this.trainData.map(data => data.y);

      const input = parseFloat(this.form.predictionX);

      if (!this.isValid(input)) {
        alert("X值必须是一个数值");
        return;
      }

      this.linearModel
        .trainModel(xs, ys)
        .then(() => {
          console.log("trainModel success");
          this.message.trainMsg = "模型训练成功";
        })
        .catch(error => {
          this.message.trainMsg = "模型训练失败";
        });
    },
    predict() {
      const input = parseFloat(this.form.predictionX);

      if (!this.isValid(input)) {
        alert("X值必须是一个数值");
        return;
      }
      console.log(input);

      this.form.predictionY = this.linearModel.predict(input);
    },
    isValid(val) {
      return val => typeof val === "number" && !Number.isNaN(val);
    }
  },
  components: {
    LinearModel
  }
};
</script>

<style scoped>
.container-border {
  margin-top: 20px;
  padding: 10px;
  width: 280px;
  border: 1px solid #ccc;
}

button {
  margin-top: 10px;
  margin-right: 10px;
}

input {
  padding: 5px;
  margin-right: 10px;
}
.fish {
  position: absolute;
  background-color: yellow;
  width: 20px;
  height: 20px;
}
</style>