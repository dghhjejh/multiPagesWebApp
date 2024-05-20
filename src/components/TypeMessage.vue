<template>
  <v-container>
    <v-card>
      <v-card-actions>
        <v-btn color="info" @click="afficherMessage">message</v-btn>
        <v-btn color="error" @click="afficherErreur">erreur</v-btn>
        <v-btn color="success" @click="afficherSuccess">success</v-btn>
      </v-card-actions>
    </v-card>
    <div class="toast-container">
        <div v-if="isMessageOpen && (!isErrorOpen && !isSuccessOpen)" class="toast info">{{ message }}</div>
        <div v-if="isErrorOpen && (!isMessageOpen && !isSuccessOpen)" class="toast error">{{ erreur }}</div>
        <div v-if="isSuccessOpen && (!isErrorOpen && !isMessageOpen)" class="toast success">{{ success }}</div>
    </div>
  </v-container>
  </template>
  <script setup>
  /* eslint-disable */
  import {defineProps, ref} from 'vue';
  const propsTypeMessage = defineProps({
    message:{
        type: String,
        required: true
    },
    erreur:{
        type:String,
        required:true
    },
    success:{
        type:String,
        required:true
    }
  })
  const isMessageOpen = ref(false);
  const message = ref('message');
  const afficherMessage = () =>{
    message.value = "ceci est un simple message";
    isMessageOpen.value = true;
    setTimeout(()=>{
        message.value = "message";
        isMessageOpen.value = false;
    }, 3000);
  };
  const erreur = ref('erreur');
  const isErrorOpen = ref(false);
  const afficherErreur = () =>{
    erreur.value = "ceci est un message d'erreur";
    isErrorOpen.value = true;
    setTimeout(()=>{
        erreur.value = "erreur";
        isErrorOpen.value = false;
    }, 3000);
  };
  const success = ref('success');
  const isSuccessOpen = ref(false);
  const afficherSuccess = () =>{
    success.value = "ceci est un succès";
    isSuccessOpen.value = true;
    setTimeout(()=>{
        success.value = "success";
        isSuccessOpen.value = false;
    }, 3000);
  };
  </script>
  
  <style>
.toast-container {
  position: fixed;
  top: 10px;
  right: 10px;
  z-index: 9999;
}

.toast {
  display: flex;
  align-items: center;
  background-color: #333;
  color: #fff;
  padding: 16px;
  border-radius: 4px;
  margin-bottom: 10px;
  animation: fadein 0.5s, fadeout 0.5s 2.5s;
}

.toast.info {
  background-color: #2196f3;
}

.toast.error {
  background-color: #f44336;
}

.toast.success {
  background-color: #4caf50;
}

@keyframes fadein {
  from { opacity: 0; }
  to { opacity: 1; }
}

@keyframes fadeout {
  from { opacity: 1; }
  to { opacity: 0; }
}
</style>