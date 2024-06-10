<template>
<div class="tout_concerne_barre_de_recherche">
      <div class="mise_en_page">
        <h1 class="texte">Selection: {{ unPays }}</h1>
        <BarreDeRechercheDropDown :source="pays" v-model="unPays"/>
      </div>
    </div>
    <div>
      <TypeMessage :message="''" :erreur="''" :success="''"/>
    </div>
    <v-container>
    <v-card>
      <v-card-actions>
        <v-btn color="info" @click="afficherMessage">message</v-btn>
        <v-btn color="error" @click="afficherErreur">erreur</v-btn>
        <v-btn color="success" @click="afficherSuccess">success</v-btn>
      </v-card-actions>
    </v-card>
    </v-container>
</template>

<script setup>
import { ref, onMounted} from 'vue';
import BarreDeRechercheDropDown from './BarreDeRechercheDropDown';
import TypeMessage from './TypeMessage';
import axios from 'axios';
const unPays = ref('');
const pays = ref([]);
const status = ref(true);
const erreur = ref(null);
onMounted(async() =>{
    try{
        const reponse = await axios.get('https://restcountries.com/v3.1/all?fields=translations');
        pays.value = reponse.data.map(lePays => lePays.translations.fra.common);
    }
    catch(err){
        erreur.value = 'une erreur est survenue: '+err.message;
    }
    finally{
        status.value = false;
    }
})
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