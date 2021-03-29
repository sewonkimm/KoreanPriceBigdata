<template>
  <div class="register">
    <div class="email" v-if="!isEmailCheck">
      <EmailInput />
      <button class="nextButton" v-on:click="isEmailCheck = !isEmailCheck">
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
import EmailInput from '@/components/register/emailInput.vue';
import PasswordInput from '@/components/register/passwordInput.vue';

export default {
  name: 'Register',
  components: {
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
