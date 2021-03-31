<template>
  <div class="register">
    <!-- 로고 -->
    <div class="logo">
      <LogoName />
    </div>
    <div class="email" v-if="!isEmailCheck">
      <EmailInput />
      <button
        :disabled="isEmailCheck == false"
        class="nextButton"
        v-on:click="isEmailCheck = !isEmailCheck"
      >
        다음
      </button>
    </div>
    <div class="password" v-if="isEmailCheck">
      <PasswordInput />
    </div>
  </div>
</template>
<script>
import '@/components/css/register/style.scss';
import { LogoName } from '@/assets/index.js';
import EmailInput from '@/components/register/emailInput.vue';
import PasswordInput from '@/components/register/passwordInput.vue';

export default {
  name: 'Register',
  components: {
    LogoName,
    EmailInput,
    PasswordInput,
  },
  data: function() {
    return {
      isEmailCheck: false,
    };
  },
  methods: {},
};
</script>
