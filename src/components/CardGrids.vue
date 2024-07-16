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
                    :value="selectedDate.toISOString().substring(0, 10)"
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
  
        <v-col cols="12" md="6" class="mx-auto">
          <v-card
            v-for="(item, indice) in taches"
            :key="indice"
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
  import { ref, onMounted } from 'vue';
  import axios from 'axios';

  const showDatePicker = ref(false);
  const titre = ref('');
  const description = ref('');
  const taches = ref([]);
  const selectedDate = ref(new Date());
  const statusGet= ref(true);
  const statusPost = ref(true);
  const statusDelete = ref(true);
  const erreur = ref(null);
  const afficherCalendrier = () => {
    showDatePicker.value = true;
  };
  
const getData = async() => {
  try{
        const response = await axios.get('http://127.0.0.1:8000/Taches');
        taches.value = response.data;
    }
    catch(err){
        erreur.value = 'une erreur est survenue: '+err.message;
    }
    finally{
        statusGet.value = false;
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
        date: selectedDate.value.toISOString().substring(0, 10),
        description: description.value
      };
      const response = await axios.post("http://127.0.0.1:8000/Taches/", dataSent);
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
      const response = await axios.delete(`http://127.0.0.1:8000/Taches/${index}`);
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
  .leconteneur {
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
  </style>