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
        <v-form class="input">
          <v-container fluid>
            <v-row>
              <v-text-field
                v-model="email"
                :rules="[rules.required, rules.email]"
                name="input-10-1"
                label="이메일"
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
// import EmailInput from '@/components/register/emailInput.vue';
import PasswordInput from '@/components/register/passwordInput.vue';

export default {
  name: 'Register',
  components: {
    LogoName,
    // EmailInput,
    PasswordInput,
  },
  data: function() {
    return {
      isActive: false, // 다음 버튼 활성화 비활성화 결정
      isEmailCheck: false,
      email: '',
      rules: {
        required: (value) => !!value || '필수로 입력해야 합니다..',
        email: (value) => {
          const pattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
          return pattern.test(value) || '이메일 형식에 맞춰 작성해주세요.';
        },
      },
    };
  },
  watch: {
    // email과 password값이 바뀔때마다 함수 실행
    email: function() {
      this.buttonActive();
    },
  },
  methods: {
    EmailCheck: function() {
      this.isEmailCheck = !this.isEmailCheck;
    },
    buttonActive: function() {
      // email과 password를 모두 입력했을 때 로그인 버튼 활성화
      if (this.email !== '') {
        this.isActive = true;
      } else this.isActive = false;
    },
  },
};
</script>
