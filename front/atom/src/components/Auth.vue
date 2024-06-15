<script setup>
import axios from 'axios';
import { useCookies } from 'vue3-cookies'
const { cookies } = useCookies();
import { useRouter } from "vue-router";
const router = useRouter();
let email;
function auth() {
    axios.post('https://rosatom.firecalculation.ru/api/user/auth/email/', {
        email: email,
    },
        {
            headers: {
                'Content-Type': 'multipart/form-data'
            }
        })
        .then(function (response) {
            cookies.set("token", response.data.token);
            cookies.set("email", email);
            const tokens = cookies.get("token");
            console.log(tokens);
            router.push({ name: 'base' });

        })
        .catch(function (error) {
            console.log(error);
        });
    console.log(email)
};
</script>
<template>
    <header>
        <div class="container">
            <h1>Росатом</h1>
            <nav>
                <ul>
                    <li><a href="#overview">Обзор</a></li>
                    <li><a href="#uranium">Уран</a></li>
                    <li><a href="#aes">АЭС</a></li>
                    <li><a href="#safety">Безопасность</a></li>
                </ul>
            </nav>
        </div>
    </header>
    <main>
        <div class="container">
            <form v-on:submit.prevent="auth">
                <div class="mb-3">
                    <label for="exampleInputEmail1" class="form-label">Email адресс</label>
                    <input v-model="email" type="email" class="form-control" id="exampleInputEmail1"
                        aria-describedby="emailHelp">
                    <div id="emailHelp" class="form-text">Для Авторизации введите свою почту.</div>
                </div>
                <button type="submit" class="btn btn-primary">Подтвердить</button>
            </form>
        </div>

    </main>
</template>

<style></style>
