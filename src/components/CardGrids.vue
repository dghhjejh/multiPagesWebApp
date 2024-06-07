<template>
    <header>
        <NavBar/>
    </header>
    <v-container class="leconteneur">
        <v-row>
           <v-col cols="12" md="8" class="mx-auto">
            <v-text-field v-model="nouvelleTache" label="Ajouter une tâche" append-icon="mdi-plus" @click:append="ajouterTache">
            </v-text-field>
           </v-col>
        </v-row>
        <v-row>
            <v-col cols="12" md="8" class="mx-auto">
                <v-card
                v-for="(tache, indice) in taches"
                :key="indice"
                class="mb-4"
                >
                <v-card-title>
                    {{ tache }}
                    <v-spacer></v-spacer>
                    <v-btn icon @click="supprimerTache(indice)">
                    <v-icon>mdi-delete</v-icon>
                    </v-btn>
                </v-card-title>
                </v-card>
            </v-col>
        </v-row>
    </v-container>
</template>

<script setup>
import NavBar from './NavBar';
import {ref} from 'vue';
const nouvelleTache = ref('');
const taches = ref([]);
const ajouterTache = () =>{
    if(nouvelleTache.value.trim() !== ''){
        taches.value.push(nouvelleTache.value);
        nouvelleTache.value = '';
    }
};

const supprimerTache = (indice) =>{
    taches.value.splice(indice, 1);
};
</script>

<style>
.leconteneur{
    position: fixed;
    top: 110px;
    z-index: 9999;
}
.mx-auto {
  margin-left: auto;
  margin-right: auto;
}
</style>