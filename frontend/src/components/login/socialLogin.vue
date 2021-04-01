<template>
  <div class="socialLogin">
    <v-dialog v-model="dialog" width="320">
      <template v-slot:activator="{ on, attrs }">
        <v-btn class="socialLoginButton" height="63" v-bind="attrs" v-on="on">
          다른 방법으로 시작하기
        </v-btn>
      </template>

      <v-card>
        <v-card-title class="title">
          다른 방법으로 시작하기
        </v-card-title>

        <div class="socialLoginButton">
          <Google />
          <Kakao />
        </div>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn text @click="dialog = false" class="closeButton">
            닫기
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>
<script>
import { Google, Kakao } from '@/assets/index.js';

export default {
  name: 'SocialLogin',
  components: {
    Google,
    Kakao,
  },
  data() {
    return {
      dialog: false,
    };
  },
};
</script>
