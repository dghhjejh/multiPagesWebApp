<template>
  <v-container class="leconteneur">
    <v-row>
      <v-col cols="12" md="6" class="mx-auto">
        <v-card class="mb-4">
          <v-card-title>
            <v-text-field v-model="titre" label="Titre de la tâche"></v-text-field>
            <v-text-field v-model="description" label="Description"></v-text-field>
            <v-menu
              v-model="showDatePicker"
              transition="scale-transition"
              min-width="auto"
              offset-y
            >
              <template v-slot:activator="{ on, attrs }">
                <v-text-field
                  :value="formattedDate"
                  v-model="showDatePicker"
                  v-bind="attrs"
                  v-on="on"
                  outlined
                  prepend-icon="mdi-calendar"
                  readonly
                  label="Sélectionner une date"
                  @click:prepend="afficherCalendrier"
                ></v-text-field>
              </template>
              <v-date-picker
                v-model="selectedDate"
                @input="showDatePicker = false"
                no-title
              ></v-date-picker>
            </v-menu>
          </v-card-title>
          <v-card-actions>
            <v-btn icon @click="postData">
              <v-icon>mdi-plus</v-icon>
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
      <LoadingSpinner v-if="isLoading"/>
      <v-col cols="12" md="6" class="mx-auto">
        <v-card
          v-for="item in taches"
          :key="item.id"
          class="mb-4"
        >
          <v-card-title>
            <div>Titre: {{ item.titre }}</div>
            <div>Description: {{ item.description }}</div>
            <div>Date: {{ item.date }}</div>
            <v-spacer></v-spacer>
            <v-btn icon @click="deleteData(item.id)">
              <v-icon>mdi-delete</v-icon>
            </v-btn>
          </v-card-title>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue';
import axios from 'axios';
import moment from 'moment-timezone';
import LoadingSpinner from './LoadingSpinner'
const showDatePicker = ref(false);
const titre = ref('');
const description = ref('');
const taches = ref([]);
const selectedDate = ref(new Date());
const statusGet= ref(true);
const statusPost = ref(true);
const statusDelete = ref(true);
const erreur = ref(null);
const isLoading = ref(true);
axios.defaults.baseURL = process.env.VUE_APP_API_URL;

const afficherCalendrier = () => {
  showDatePicker.value = true;
};

const formattedDate = computed(() => {
  return moment(selectedDate.value).tz('America/Toronto').format('YYYY-MM-DD');
});

const getData = async() => {
try{
      const response = await axios.get('/Taches');
      console.log(response.data)
      taches.value = response.data;
  }
  catch(err){
      erreur.value = 'une erreur est survenue: '+err.message;
  }
  finally{
      statusGet.value = false;
      isLoading.value = false;
  }
}
onMounted(async() =>{
  getData();
});

const postData = async() =>{
await getData();
if(titre.value.trim() !== ''){
  try{
    const dataSent = {
      titre: titre.value,
      date: moment(selectedDate.value).tz('America/Toronto').format('YYYY-MM-DD'),
      description: description.value
    };
    const response = await axios.post("/Taches/", dataSent);
    console.log(response.data)
    await getData();
    titre.value = "";
    description.value = "";
}
  catch(err){
    erreur.value = 'une erreur est survenue: '+err.message;
 }
 finally{
    statusPost.value = false;
 }
}
}
const deleteData = async(index) => {
  try{
    await getData();
    const response = await axios.delete(`/Taches/${index}`);
    console.log(response.data);
    await getData();
  }
  catch(err){
    erreur.value = 'une erreur est survenue: '+err.message;
 }
 finally{
    statusDelete.value = false;
 }
}
</script>

<style scoped>
  .leconteneur{
    position: relative;
    top: 110px;
    z-index: 1;
  }
  .mx-auto {
    margin-left: auto;
    margin-right: auto;
  }
  .v-menu__content {
    z-index: 3000 !important;
  }
  .spinner-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}
</style>