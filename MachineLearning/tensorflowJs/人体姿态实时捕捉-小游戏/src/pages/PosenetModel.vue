<template>
  <div class="page">
    <h2>使用tensoleflow.js pOSENET模型训练。</h2>

    <div className="fish-tank">
      <video
        class="video"
        playsInline
        ref="video"
      />
      <img
        ref="fish"
        width="200px"
        class="fish"
        :class="toMirror"
        :style="fishStyle"
        :src="IMAGE"
      />
    </div>

  </div>
</template>

<script>
import * as posenet from "@tensorflow-models/posenet";
import PosenetModelData from "@/components/classes/PosenetModelData";
// Constants,
const MILLISECONDS = 500;
const imageScaleFactor = 0.5;
const outputStride = 16;
const flipHorizontal = true;
const maxVideoSize = 300;
const weight = 0.5;
const initialPosition = 40;
const offset = 40;

export default {
  data() {
    return {
      state: {
        top: initialPosition,
        left: initialPosition,
        oldTop: initialPosition,
        oldLeft: initialPosition
      },
      IMAGE: "https://aralroca.github.io/fishFollow-posenet-tfjs/fish.gif",
      timeout: "",
      video: "",
      videoElement: "",
      net: "",
      toMirror: "",
      fishStyle: {
        left: '450px',
        top: '450px'
      }
    };
  },
  computed: {
    computedState: function() {
      return this.state;
    }
  },
  methods: {
    async initLoad() {
      this.net = await posenet.load(weight);
      this.setRef();
      this.initCapture();
    },
    initCapture() {
      this.timeout = setTimeout(this.capture, MILLISECONDS);
    },

    async capture() {
      let nose;
      if (!this.videoElement || !this.net) {
        this.initCapture();
        return;
      }

      if (!this.video && this.videoElement) {
        this.video = await this.loadVideo(this.videoElement);
      }

      const poses = await this.net.estimateSinglePose(
        this.video,
        imageScaleFactor,
        flipHorizontal,
        outputStride
      );

      if (poses && poses.keypoints) {
        nose = poses.keypoints.filter(keypoint => keypoint.part === "nose")[0];
      }

      if (nose) {
        this.toMirror = this.state.oldLeft > this.state.left;
        this.state = {
          top: nose.position.y + maxVideoSize +offset,
          left: nose.position.x +maxVideoSize +offset,
          oldTop: this.state.top,
          oldLeft: this.state.left
        };

        this.fishStyle = {
          top: this.state.top +'px',
          left: this.state.left+'px'
        };
      }

      this.initCapture();
    },
    async setupCamera(videoElement) {
      videoElement.width = maxVideoSize;
      videoElement.height = maxVideoSize;

      if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
        const mobile = this.isMobile();
        const stream = await navigator.mediaDevices.getUserMedia({
          audio: false,
          video: {
            facingMode: "user",
            width: mobile ? undefined : maxVideoSize,
            height: mobile ? undefined : maxVideoSize
          }
        });
        videoElement.srcObject = stream;

        return new Promise(resolve => {
          videoElement.onloadedmetadata = () => {
            resolve(videoElement);
          };
        });
      } else {
        const errorMessage =
          "This browser does not support video capture, or this device does not have a camera";
        alert(errorMessage);
        return Promise.reject(errorMessage);
      }
    },
    async loadVideo() {
      const video = await this.setupCamera(this.videoElement);
      video.play();
      return video;
    },
    async setRef() {
      this.videoElement = document.querySelector(".video");
    },
    isMobile() {
      const isAndroid = /Android/i.test(navigator.userAgent);
      const isiOS = /iPhone|iPad|iPod/i.test(navigator.userAgent);

      return isAndroid || isiOS;
    }
  },
  mounted() {
    // 初始化，加载模型
    this.initLoad();
  },
  components: {}
};
</script>

<style scoped>
body {
  background-color: rgb(96, 125, 139);
  background-image: url("../../public/haidi.jpg");
  overflow: hidden;
}

.video {
  transform: scaleX(-1);
  opacity: 0.4;
}

.mirror {
  -moz-transform: scaleX(-1);
  -o-transform: scaleX(-1);
  -webkit-transform: scaleX(-1);
  transform: scaleX(-1);
  filter: FlipH;
  -ms-filter: "FlipH";
}
.fish-tank {
  position: relative;
  width: 100vw;
  height: 100vh;
  margin: -10px 0 0 0;
}
.fish {
  position: absolute;
  transition-duration: 2s;
  top: 450px;
  left: 450px;
}
</style>