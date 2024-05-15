
<template>
   <div class="menu-item" @click="toggleDropdown">
    <a href="#">
        {{ title }}
    </a>
    <transition name="fade" appear>
        <div class="sub-menu" v-if="isOpen">
            <div v-for= "(item,i) in items" :key="i" class="menu-item">
                <a :href="item.link">{{ item.title }}</a>
            </div>
        </div>
    </transition>
   </div>
</template>

<script>
/* eslint-disable */
  export default {
    name:"dropdown",
    props: ["title", "items"],
    data(){
        return{
            isOpen:false
        }
    },
    methods: {
        toggleDropdown() {
            this.isOpen = !this.isOpen;
            if (this.isOpen) {
                setTimeout(() => {
                    this.isOpen = false;
                }, 10000);
            }
        }
    }
  }
</script>

<style>
nav .menu-item .sub-menu{
    position:absolute;
    background-color: #222;
    top: calc(100% + 18px);
    left: 50px;
    transform: translateX(-50%);
    width: max-content;
    border-radius: 0px 0px 16px 16px;
}
.fade-enter-active,
.fade-leave-enter{
    transition: all .5s ease-out;
}
.fade-enter,
.fade-leave-to{
    opacity: 0;
}
</style>