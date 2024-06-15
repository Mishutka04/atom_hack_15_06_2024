<script setup>
import { ref, onMounted } from 'vue';
import { useRouter } from "vue-router";
import voice_start from '../audio/voice_start.mp3';
import voice_translate from '../audio/voice_translate.mp3';
import voice_update from '../audio/voice_update.mp3';
import voice_not_answer from '../audio/voice_not_answer.mp3';
import axios from 'axios';
import setMessages from "./Base.vue";
const transcript = ref('');
const isRecording = ref(false);
const status = ref('');
let statusMicro = true;
let statusVoice = true;
const Recognition = window.SpeechRecognition || window.webkitSpeechRecognition;
const sr = new Recognition();
const router = useRouter();
const props = defineProps({
    select_chat_id: Number,
    token: String
});

const emit = defineEmits(["setData"]);
onMounted(() => {
    sr.continuous = true,
        sr.interimResults = true

    sr.onstart = () => {
        isRecording.value = true
    }

    sr.onend = () => {
        if (statusVoice) {
            statusVoice = false;
            var data = {};
            const audio = new Audio(voice_update);
            audio.play();

            let text = transcript.value.charAt(0).toUpperCase() + transcript.value.slice(1, transcript.value.length - 1);
            emit("setUserText", text);
            console.log(text);
            axios.post('https://rosatom.firecalculation.ru/api/support/messages/', { is_user_message: true, text: text, dialog: props.select_chat_id }, { headers: { Authorization: "Token " + props.token } })
                .then(response => {
                    {
                        emit("setData", response.data);
                        emit("setUserText", null);
                        statusVoice = true;
                    }
                })
                .catch(function (error) {
                    console.log(error);
                    statusVoice = true;
                });
        }

        // axios.get('http://127.0.0.1:8000/api/events/events/?search=' + transcript.value.charAt(0).toUpperCase() + transcript.value.slice(1, transcript.value.length - 1)).then(response => {
        //     data = response.data.slice(0, 2)[0];
        //     console.log(transcript.value.charAt(0).toUpperCase() + transcript.value.slice(1, transcript.value.length - 1));
        // }).catch(function (error) { });
        // setTimeout(() => {
        //     if (data) {
        //         router.push('/description/' + data.id);
        //         const audio = new Audio(voice_translate);
        //         audio.play();
        //     } else {
        //         const audio = new Audio(voice_not_answer);
        //         audio.play();
        //     }
        // }, 2000);

        isRecording.value = false
    }

    sr.onresult = (evt) => {
        for (let i = 0; i < evt.results.length; i++) {
            const result = evt.results[i]
            if (result.isFinal) CheckForCommand(result)
        }
        const t = Array.from(evt.results)
            .map(result => result[0])
            .map(result => result.transcript)
            .join('')
        transcript.value = t
    }
})

const CheckForCommand = (result) => {
    const t = result[0].transcript;
    if (t.includes('stop recording')) {
        sr.stop()
    } else if (
        t.includes('what is the time') ||
        t.includes('what\'s the time')
    ) {
        sr.stop()
        alert(new Date().toLocaleTimeString())
        setTimeout(() => sr.start(), 100)
    }
}

const ToggleMic = () => {
    const audio = new Audio(voice_start); // path to file
    audio.play();
    setTimeout(() => {
        if (isRecording.value) {
            sr.stop()
        } else {
            sr.start()
        }
    }, 5000);

}
</script>

<template>

    <a :class="`mic`" @click="ToggleMic"><img src="../assets/micro.svg" alt="" width="40px" height="40px"></a>
</template>

<style></style>