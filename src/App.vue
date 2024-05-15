
<template>
  <div id="app">
    <header>
      <NavBar/>
    </header>
    <div class="tout_concerne_barre_de_recherche">
      <div class="mise_en_page">
        <h1 class="texte">Selection: {{ unPays }}</h1>
        <BarreDeRechercheDropDown :source="pays" v-model="unPays"/>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import {Flip, toast} from "vue3-toastify";
import "vue3-toastify/dist/index.css";
import NavBar from './components/NavBar';
import BarreDeRechercheDropDown from './components/BarreDeRechercheDropDown';
import pays from './pays/pays.json';
toast("Bienvenue sur ma page!", {
  "theme": "light",
  autoClose: 1000,
  transition: Flip,
})
const unPays = ref('');
</script>
<style>
*{
  margin: 0;
  padding: 0;
  box-sizing:border-box;
}
.tout_concerne_barre_de_recherche{
  width: 100vw;
  height:100vh;
  background-color: #edf2f7;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}
header{
  position:fixed;
  width: 100vw;
  background-color: #222;
  padding: 15px;
}
.mise_en_page{
  width: calc(100% / 4);
}
.texte{
  text-align: center;
  font-weight: bold;
  justify-content: space-between;
}
</style>
