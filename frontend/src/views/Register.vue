<template>
  <div class="register">
    <!-- 로고 -->
    <div class="logo">
      <LogoName />
    </div>
    <div class="emailForm" v-if="!isEmailCheck">
      <div class="emailInput">
        <div class="informationMessage">
          <h1>이메일을 입력해주세요</h1>
        </div>
        <v-form class="emailInputForm">
          <v-container fluid>
            <v-row>
              <v-text-field
                v-model="email"
                :rules="emailRules"
                label="이메일"
                required
              ></v-text-field>
            </v-row>
          </v-container>
        </v-form>
      </div>
      <v-btn
        @click="EmailCheck()"
        :class="{ active: isActive, nextButton: 'nextButton' }"
        height="63"
        >다음</v-btn
      >
    </div>
    <div class="password" v-if="isEmailCheck">
      <PasswordInput />
    </div>
  </div>
</template>
<script>
import '@/components/css/register/style.scss';
import { LogoName } from '@/assets/index.js';
import PasswordInput from '@/components/register/passwordInput.vue';

export default {
  name: 'Register',
  components: {
    LogoName,
    PasswordInput,
  },
  data: function() {
    return {
      isActive: false, // 다음 버튼 활성화 비활성화 결정
      isEmailCheck: false,
      email: '',
      emailRules: [
        (value) =>
          /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(
            value
          ) || '이메일 형식에 맞춰 작성해주세요.',
      ],
    };
  },
  watch: {
    email: function() {
      this.buttonActive();
    },
  },
  methods: {
    EmailCheck: function() {
      this.isEmailCheck = !this.isEmailCheck;
    },
    buttonActive: function() {
      if (this.email !== '') {
        this.isActive = true;
      } else this.isActive = false;
    },
  },
};
</script>
