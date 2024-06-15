<script>
import axios from 'axios';
import { useCookies } from 'vue3-cookies'
const { cookies } = useCookies();
import Voice from './Voice.vue';
export default {
    components: {
        Voice
    },
    data() {
        return {
            email: cookies.get("email"),
            flag: 'start',
            select_group_id: null,
            select_chat_id: null,
            user_message: null,
            group: null, chats: null,
            messages: null,
            tokens: null,
            text_user: null,
            auth_user: false,
            model: "qween",
            bers_user_text: null
        }
    },
    mounted() {
        axios.post('https://rosatom.firecalculation.ru/api/auth/token/', { token: cookies.get("token"), email: cookies.get("email") })
            .then(response => {
                {
                    this.tokens = response.data.token,
                        axios.get('https://rosatom.firecalculation.ru/api/support/prompts/')
                            .then(response => {
                                {

                                    this.group = response.data;
                                    this.auth_user = true;

                                }
                            })
                            .catch(function (error) {
                                console.log(error);
                            });

                }
            })
            .catch(function (error) {
                console.log(error);
            });
        this.$nextTick(this.scrollToLastMessage);
    },
    methods: {
        selectBERT(){
            this.model = "bert";
            this.flag = 'chat'
        },
        setForUser(messages) {
            this.user_message = messages
            this.scrollToLastMessage();
        },
        scrollToLastMessage() {
            this.$nextTick(() => {
                const chatContainer = this.$el.querySelector('.chat_messages');
                if (chatContainer) {
                    chatContainer.scrollTop = chatContainer.scrollHeight;
                }
            });
        },
        closeHelp() {
            this.flag = 'start';
        },
        setMessages(messages) {
            this.messages = messages;
            this.scrollToLastMessage(); // Прокрутка до последнего сообщения при выборе чата
        },
        createChat() {
            console.log(this.select_group_id)
            axios.post('https://rosatom.firecalculation.ru/api/support/dialogs/', { prompt: this.select_group_id }, { headers: { Authorization: "Token " + this.tokens } })
                .then(response => {
                    {

                        this.messages = null;
                        this.select_chat_id = response.data.id;
                        this.flag = 'chat';
                    }
                })
                .catch(function (error) {
                    console.log(error);
                });
        },
        select_chat(id) {
            axios.get('https://rosatom.firecalculation.ru/api/support/dialogs/' + id, { headers: { Authorization: "Token " + this.tokens } })
                .then(response => {
                    {

                        this.messages = response.data.messages;
                        this.select_chat_id = id;
                        this.flag = 'chat';
                        console.log(response.data.messages)
                        this.scrollToLastMessage(); // Прокрутка до последнего сообщения при выборе чата
                    }
                })
                .catch(function (error) {
                    console.log(error);
                });
        },
        select_chats(id) {
            this.model = "qween"
            this.select_group_id = id;
            axios.get('https://rosatom.firecalculation.ru/api/support/dialogs/', { headers: { Authorization: "Token " + this.tokens } })
                .then(response => {
                    {
                        this.chats = response.data;
                        this.flag = "chats"
                    }
                })
                .catch(function (error) {
                    console.log(error);
                });

        },
        open_chat() {
            this.flag = 'group';
        },
        send_messages(text) {
            console.log(this.model)
            if (!this.user_message) {
                this.text_user = null;
                this.user_message = text;
                if(this.model != "bert"){
                axios.post('https://rosatom.firecalculation.ru/api/support/messages/', { is_user_message: true, text: text, dialog: this.select_chat_id }, { headers: { Authorization: "Token " + this.tokens } })
                    .then(response => {
                        {
                            this.messages = response.data;
                            this.user_message = null;
                            this.scrollToLastMessage(); // Прокрутка до последнего сообщения при выборе чата
                            console.log("88", response.data)

                        }
                    })
                    .catch(function (error) {
                        console.log(error);
                    });}
                    else{
                        this.text_user = null;
                this.user_message = text;
                console.log("BERT ON!")
                axios.post('https://rosatom.firecalculation.ru/api/support/questions-answers/', { question: text }, { headers: { Authorization: "Token " + this.tokens } })
                    .then(response => {
                        {
                            this.messages = response.data;
                            console.log(response.data)
                            this.user_message = null;
                            this.scrollToLastMessage(); // Прокрутка до последнего сообщения при выборе чата
                            console.log(213)

                        }
                    })
                    .catch(function (error) {
                        console.log(error);
                    });
                    }
            } else {
                console.log("НЕ СПАМЬ!")
            }
        }
    }
}
</script>

<template>
    <div class="container2">
        <header>
            <div class="container">
                <nav>
                    <ul class="nav">
                        <li class="nav-item">
                            <a class="nav-link" href="#"><img
                                    src="https://www.rosatom.ru//upload/new_logo_main/Rosatom_Vertical_ru.svg"
                                    alt="Росатом" width="100px" height="100px"></a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="#">О Росатоме</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="#">Направления деятельности</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link disabled" href="#">Журналистам</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link disabled" href="#">Карьера</a>
                        </li>
                    </ul>

                </nav>
            </div>
        </header>
        <main>
            <section id="overview">
                <div class="banner-container">
                    <div class="banner">
                        <img src="https://www.rosatom.ru/upload/medialibrary/a56/a563ea52572fc1c26af229aab20a3992.jpg"
                            alt="Ядерная энергетика">
                        <h1>Ядерная энергетика</h1>
                    </div>
                </div>
            </section>
            <div class="grid-container">
                <div class="grid">
                    <div class="grid-item" data-number="01">Добыча урана</div>
                    <div class="grid-item" data-number="02">Обогащение урана</div>
                    <div class="grid-item" data-number="03">Проектирование, инжиниринг и строительство АЭС</div>
                    <div class="grid-item" data-number="04">Генерация электроэнергии</div>
                    <div class="grid-item" data-number="05">Сервис и обслуживание АЭС</div>
                    <div class="grid-item" data-number="06">Ядерная и радиационная безопасность</div>
                    <div class="grid-item" data-number="07">Атомные станции большой мощности</div>
                    <div class="grid-item" data-number="08">Атомные станции малой мощности</div>
                </div>
            </div>
            <div class="social">
                <div class="social_items">
                    <span>Поделиться:</span>
                    <img src="https://upload.wikimedia.org/wikipedia/commons/2/21/VK.com-logo.svg" alt="VK">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/8/82/Telegram_logo.svg" alt="Twitter">
                </div>
            </div>
            <div class="news">
                <div class="news-section">
                    <div class="news-item">
                        <span class="date">27 мая 2024</span>
                        <h3>Российская Федерация и Узбекистан подписали соглашение о строительстве атомной станции малой
                            мощности</h3>
                        <p>Подробнее</p>
                    </div>
                    <div class="news-item">
                        <span class="date">7 июня 2024</span>
                        <h3>Павильон «Атом» приглашает на эждень «Зеленый атом»</h3>
                        <p>Подробнее</p>
                    </div>
                    <div class="news-item">
                        <span class="date">6 июня 2024</span>
                        <h3>«Атомэнергопром» и ВТБ подписали кредитное соглашение 50 млрд руб.</h3>
                        <p>Подробнее</p>
                    </div>
                    <div class="news-item">
                        <span class="date">21 мая 2024</span>
                        <h3>Председатель Правительства РФ Михаил Мишустин посетил Саров</h3>
                        <p>Подробнее</p>
                    </div>
                </div>
            </div>
        </main>

        <footer>
            <div class="container">
                <p>&copy; 2024 Росатом. Все права защищены.</p>
            </div>
        </footer>
        <div v-if="flag == 'chat'" class="chat_block">
            <div class="chat_title">
                <div></div>
                <div class="chat_title_text">Atom Assist<br />Ядерная поддержка в реальном времени</div>
                <div @click="closeHelp"><img src="../assets/out.svg" alt="" width="40px" height="40px"></div>
            </div>
            <div class="chat">
                <div class="chat_messages">
                    <div v-for="(message, index) in messages" :key='index' v-if="messages && model=='qween'">
                        <div v-if="!message.is_user_message" class="left_message">
                            <div class="left_elements">
                            <div class="message left_text">{{ message.text }}</div>
                            <div class="answer_accept">Вас удовлетворил ответ?</div>
                            <div class="enjoy">
                                <div class="dislike"><img src="../assets/like.svg" alt="" width="70px" height="70px"> </div>
                                <div class="like"><img src="../assets/dislike.svg" alt="" width="70px" height="70px"></div>
                            </div>
                        </div>
                            
                        </div>
                        <div v-else class="right_message">
                            <div class="message right_text">{{ message.text }}</div>
                            

                        </div>
                    </div>
                    <div v-for="(message, index) in messages" :key='index' v-if="messages && model=='bert'">
                        <div v-if="!message.is_user_message" class="left_message">
                            <div class="left_elements">
                            <div class="message left_text">{{ message.answer }}</div>
                        </div>
                            
                        </div>
                        <div v-else class="right_message">
                            <div class="message right_text">{{ bers_user_text }}</div>
                            

                        </div>
                    </div>
                    <div v-if="user_message">

                        <div class="right_message">
                            <div class="message right_text">{{ user_message }}</div>

                        </div>
                        <div class="left_message">
                            <div class="message left_text">Ожидайте, обрабатываю запрос</div>
                        </div>
                    </div>

                </div>


                <div class="chat_form">
                    <textarea v-model="text_user" class="textareaElement"></textarea>
                    <div>

                        <Voice :select_chat_id="select_chat_id" :token="tokens" @setData="setMessages"
                            @setUserText="setForUser" />
                    </div>
                    <div @click="send_messages(text_user)"><img src="../assets/send.svg" alt="" width="40px"
                            height="40px">
                    </div>
                </div>
            </div>
        </div>
        
        <div v-if="flag == 'group'" class="chat_block">
            <div class="chat_title">
                <div class="assist-2" v-if="auth_user"><button type="button" @click="selectBERT" class="btn btn-primary">Assist 2.0</button></div>
                <div class="chat_title_text">Atom Assist<br />Ядерная поддержка в реальном времени<br />Выберите
                    категорию для обращения</div>
                <div @click="closeHelp"><img src="../assets/out.svg" alt="" width="40px" height="40px"></div>
            </div>
            <div class="group_chat">
                <div v-for="(item, index) in group" :key='index' v-if="group && auth_user">
                    <div @click="select_chats(item.id)" class="group_item">
                        <div class="icon"><img src="../assets/bot_logo.jpg" alt="" width="40px" height="40px"></div>
                        <div class="group_item_description">
                            <div class="group_item_type">{{ item.title }}</div>
                        </div>
                    </div>
                </div>
                <div class="not_auth" v-else>
                    <div> Уважаемый пользователь, для использования чата вам необходимо. </div>
                    <div><a href="/#/auth/">авторизироваться</a></div>
                </div>
            </div>
        </div>
        <div v-if="flag == 'chats'" class="chat_block">
            <div class="chat_title">
                <div></div>
                <div class="chat_title_text">Atom Assist<br />Ядерная поддержка в реальном времени<br />Выберите чат
                </div>
                <div @click="closeHelp"><img src="../assets/out.svg" alt="" width="40px" height="40px"></div>
            </div>
            <div class="group_elements">
                <div class="group_chat">
                    <div v-for="(item, index) in chats" :key='index' v-if="chats">
                        <div @click="select_chat(item.id)" class="group_item" v-if="item.prompt == select_group_id">
                            <div class="icon"><img src="../assets/bot_logo.jpg" alt="" width="40px" height="40px"></div>
                            <div class="group_item_description">
                                <div class="group_item_type">Обращение № {{ index + 1 }}</div>
                            </div>
                        </div>
                    </div>
                </div>
                <div @click="createChat" class="create_chat"><button type="button" class="btn btn-primary">Создать
                        чат</button></div>
            </div>
        </div>
        <div v-if="flag == 'start'">
            <div class="help_icon" @click="open_chat()">
                <div class="icon"><img src="../assets/help_icon.svg" alt="" width="60px" height="60px"></div>
            </div>
        </div>
    </div>
</template>

<style></style>
