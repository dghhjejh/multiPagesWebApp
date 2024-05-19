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
    <div>
      <TypeMessage :message="''" :erreur="''" :success="''"/>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import NavBar from './components/NavBar';
import BarreDeRechercheDropDown from './components/BarreDeRechercheDropDown';
import TypeMessage from './components/TypeMessage';
import pays from './pays/pays.json';
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