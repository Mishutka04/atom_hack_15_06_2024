<script>
import Chart from 'chart.js/auto';
export default {
    data() {


    },
    mounted() {
        new Chart(document.getElementById('myChart1'), {
                type: 'bar',
                data: {
                    labels: ["Fas"],
                    datasets: [{
                        label: 'Километраж',
                        data: [1],
                        backgroundColor: [
                            'rgba(97, 94, 252, 0.8)',
                            'rgba(199, 56, 189, 0.8)',
                            'rgba(254, 122, 54, 0.8)',
                            'rgba(54, 82, 173, 0.8)',
                        ],

                        borderWidth: 3
                    }]
                },

            }),
            new Chart(document.getElementById('myChart2'), {
                type: 'bar',
                data: {
                    labels: ["Fas"],
                    datasets: [{
                        label: 'Километраж',
                        data: [1],
                        backgroundColor: [
                            'rgba(97, 94, 252, 0.8)',
                            'rgba(199, 56, 189, 0.8)',
                            'rgba(254, 122, 54, 0.8)',
                            'rgba(54, 82, 173, 0.8)',
                        ],

                        borderWidth: 3
                    }]
                },

            })
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
        <div class="container-fluid">
            <div class="row">
                <div class="col">
                    <div class="stat-item">
                        <div class="stat-items-up">
                            <div class="stat_prot">
                                <div class="stat_prot_title">Качество</div>
                                <div class="stat_prot_elem">10%</div>
                            </div>
                            <div class="stat_prot">
                                <div class="stat_prot_title">Запросы</div>
                                <div class="stat_prot_elem">10%</div>
                            </div>
                            <div class="stat_prot">
                                <div class="stat_prot_title">Лайк / Дизлайк</div>
                                <div class="stat_prot_elem">10 / 90</div>
                            </div>
                        </div>
                        <div class="stat-items-down">
                            <div class="">Лайки - Дизлайки</div>
                            <div class="progress_bar">
                                <progress class="amount-progress" value="90" max="100">70 %</progress>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col">
                    <div class="stat-item">
                        <div class="stat-items-up">
                            <div class="stat_prot">
                                <div class="stat_prot_title">Качество</div>
                                <div class="stat_prot_elem">10%</div>
                            </div>
                            <div class="stat_prot">
                                <div class="stat_prot_title">Запросы</div>
                                <div class="stat_prot_elem">10%</div>
                            </div>
                            <div class="stat_prot">
                                <div class="stat_prot_title">Лайк / Дизлайк</div>
                                <div class="stat_prot_elem">10 / 90</div>
                            </div>
                        </div>
                        <div class="stat-items-down">
                            <div class="">Лайки - Дизлайки</div>
                            <div class="progress_bar">
                                <progress class="amount-progress" value="90" max="100">70 %</progress>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col">
                    <div class="stat-item">
                        <div class="stat-items-up">
                            <div class="stat_prot">
                                <div class="stat_prot_title">Качество</div>
                                <div class="stat_prot_elem">10%</div>
                            </div>
                            <div class="stat_prot">
                                <div class="stat_prot_title">Запросы</div>
                                <div class="stat_prot_elem">10%</div>
                            </div>
                            <div class="stat_prot">
                                <div class="stat_prot_title">Лайк / Дизлайк</div>
                                <div class="stat_prot_elem">10 / 90</div>
                            </div>
                        </div>
                        <div class="stat-items-down">
                            <div class="">Лайки - Дизлайки</div>
                            <div class="progress_bar">
                                <progress class="amount-progress" value="90" max="100">70 %</progress>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="row">
                <div class="col">
                    <div class="stat-item">
                        <div class="stat-items-up">
                            <div class="stat_prot">
                                <div class="stat_prot_title">Качество</div>
                                <div class="stat_prot_elem">10%</div>
                            </div>
                            <div class="stat_prot">
                                <div class="stat_prot_title">Запросы</div>
                                <div class="stat_prot_elem">10%</div>
                            </div>
                            <div class="stat_prot">
                                <div class="stat_prot_title">Лайк / Дизлайк</div>
                                <div class="stat_prot_elem">10 / 90</div>
                            </div>
                        </div>
                        <div class="stat-items-down">
                            <div class="">Лайки - Дизлайки</div>
                            <div class="progress_bar">
                                <progress class="amount-progress" value="90" max="100">70 %</progress>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col">
                    <div class="stat-item">
                        <div class="stat-items-up">
                            <div class="stat_prot">
                                <div class="stat_prot_title">Качество</div>
                                <div class="stat_prot_elem">10%</div>
                            </div>
                            <div class="stat_prot">
                                <div class="stat_prot_title">Запросы</div>
                                <div class="stat_prot_elem">10%</div>
                            </div>
                            <div class="stat_prot">
                                <div class="stat_prot_title">Лайк / Дизлайк</div>
                                <div class="stat_prot_elem">10 / 90</div>
                            </div>
                        </div>
                        <div class="stat-items-down">
                            <div class="">Лайки - Дизлайки</div>
                            <div class="progress_bar">
                                <progress class="amount-progress" value="90" max="100">70 %</progress>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col">
                    <div class="stat-item">
                        <div class="stat-items-up">
                            <div class="stat_prot">
                                <div class="stat_prot_title">Качество</div>
                                <div class="stat_prot_elem">10%</div>
                            </div>
                            <div class="stat_prot">
                                <div class="stat_prot_title">Запросы</div>
                                <div class="stat_prot_elem">10%</div>
                            </div>
                            <div class="stat_prot">
                                <div class="stat_prot_title">Лайк / Дизлайк</div>
                                <div class="stat_prot_elem">10 / 90</div>
                            </div>
                        </div>
                        <div class="stat-items-down">
                            <div class="">Лайки - Дизлайки</div>
                            <div class="progress_bar">
                                <progress class="amount-progress" value="90" max="100">70 %</progress>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="row">
                <div class="col">
                    <div class="stat-item">
                        <div class="stat-items-up">
                            <div class="stat_prot">
                                <div class="stat_prot_title">Качество</div>
                                <div class="stat_prot_elem">10%</div>
                            </div>
                            <div class="stat_prot">
                                <div class="stat_prot_title">Запросы</div>
                                <div class="stat_prot_elem">10%</div>
                            </div>
                            <div class="stat_prot">
                                <div class="stat_prot_title">Лайк / Дизлайк</div>
                                <div class="stat_prot_elem">10 / 90</div>
                            </div>
                        </div>
                        <div class="stat-items-down">
                            <div class="">Лайки - Дизлайки</div>
                            <div class="progress_bar">
                                <progress class="amount-progress" value="90" max="100">70 %</progress>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col">
                    <div class="stat-item">
                        <div class="stat-items-up">
                            <div class="stat_prot">
                                <div class="stat_prot_title">Качество</div>
                                <div class="stat_prot_elem">10%</div>
                            </div>
                            <div class="stat_prot">
                                <div class="stat_prot_title">Запросы</div>
                                <div class="stat_prot_elem">10%</div>
                            </div>
                            <div class="stat_prot">
                                <div class="stat_prot_title">Лайк / Дизлайк</div>
                                <div class="stat_prot_elem">10 / 90</div>
                            </div>
                        </div>
                        <div class="stat-items-down">
                            <div class="">Лайки - Дизлайки</div>
                            <div class="progress_bar">
                                <progress class="amount-progress" value="90" max="100">70 %</progress>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col">
                    <div class="stat-item">
                        <div class="stat-items-up">
                            <div class="stat_prot">
                                <div class="stat_prot_title">Качество</div>
                                <div class="stat_prot_elem">10%</div>
                            </div>
                            <div class="stat_prot">
                                <div class="stat_prot_title">Запросы</div>
                                <div class="stat_prot_elem">10%</div>
                            </div>
                            <div class="stat_prot">
                                <div class="stat_prot_title">Лайк / Дизлайк</div>
                                <div class="stat_prot_elem">10 / 90</div>
                            </div>
                        </div>
                        <div class="stat-items-down">
                            <div class="">Лайки - Дизлайки</div>
                            <div class="progress_bar">
                                <progress class="amount-progress" value="90" max="100">70 %</progress>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="row">
                <div class="col">
                    <div class="stat-item">
                        <div class="stat-items-up">
                            <div class="stat_prot">
                                <div class="stat_prot_title">Качество</div>
                                <div class="stat_prot_elem">10%</div>
                            </div>
                            <div class="stat_prot">
                                <div class="stat_prot_title">Запросы</div>
                                <div class="stat_prot_elem">10%</div>
                            </div>
                            <div class="stat_prot">
                                <div class="stat_prot_title">Лайк / Дизлайк</div>
                                <div class="stat_prot_elem">10 / 90</div>
                            </div>
                        </div>
                        <div class="stat-items-down">
                            <div class="">Лайки - Дизлайки</div>
                            <div class="progress_bar">
                                <progress class="amount-progress" value="90" max="100">70 %</progress>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col">
                    <div class="stat-item">
                        <div class="stat-items-up">
                            <div class="stat_prot">
                                <div class="stat_prot_title">Качество</div>
                                <div class="stat_prot_elem">10%</div>
                            </div>
                            <div class="stat_prot">
                                <div class="stat_prot_title">Запросы</div>
                                <div class="stat_prot_elem">10%</div>
                            </div>
                            <div class="stat_prot">
                                <div class="stat_prot_title">Лайк / Дизлайк</div>
                                <div class="stat_prot_elem">10 / 90</div>
                            </div>
                        </div>
                        <div class="stat-items-down">
                            <div class="">Лайки - Дизлайки</div>
                            <div class="progress_bar">
                                <progress class="amount-progress" value="90" max="100">70 %</progress>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col">
                    <div class="stat-item">
                        <div class="stat-items-up">
                            <div class="stat_prot">
                                <div class="stat_prot_title">Качество</div>
                                <div class="stat_prot_elem">10%</div>
                            </div>
                            <div class="stat_prot">
                                <div class="stat_prot_title">Запросы</div>
                                <div class="stat_prot_elem">10%</div>
                            </div>
                            <div class="stat_prot">
                                <div class="stat_prot_title">Лайк / Дизлайк</div>
                                <div class="stat_prot_elem">10 / 90</div>
                            </div>
                        </div>
                        <div class="stat-items-down">
                            <div class="">Лайки - Дизлайки</div>
                            <div class="progress_bar">
                                <progress class="amount-progress" value="90" max="100">70 %</progress>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="row">
                <div class="col">
                    <div class="stat-item">
                        <div class="stat-items-up">
                            <div class="stat_prot">
                                <div class="stat_prot_title">Качество</div>
                                <div class="stat_prot_elem">10%</div>
                            </div>
                            <div class="stat_prot">
                                <div class="stat_prot_title">Запросы</div>
                                <div class="stat_prot_elem">10%</div>
                            </div>
                            <div class="stat_prot">
                                <div class="stat_prot_title">Лайк / Дизлайк</div>
                                <div class="stat_prot_elem">10 / 90</div>
                            </div>
                        </div>
                        <div class="stat-items-down">
                            <div class="">Лайки - Дизлайки</div>
                            <div class="progress_bar">
                                <progress class="amount-progress" value="90" max="100">70 %</progress>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col">
                    <div class="stat-item">
                        <div class="stat-items-up">
                            <div class="stat_prot">
                                <div class="stat_prot_title">Качество</div>
                                <div class="stat_prot_elem">10%</div>
                            </div>
                            <div class="stat_prot">
                                <div class="stat_prot_title">Запросы</div>
                                <div class="stat_prot_elem">10%</div>
                            </div>
                            <div class="stat_prot">
                                <div class="stat_prot_title">Лайк / Дизлайк</div>
                                <div class="stat_prot_elem">10 / 90</div>
                            </div>
                        </div>
                        <div class="stat-items-down">
                            <div class="">Лайки - Дизлайки</div>
                            <div class="progress_bar">
                                <progress class="amount-progress" value="90" max="100">70 %</progress>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col">
                    <div class="stat-item">
                        <div class="stat-items-up">
                            <div class="stat_prot">
                                <div class="stat_prot_title">Качество</div>
                                <div class="stat_prot_elem">10%</div>
                            </div>
                            <div class="stat_prot">
                                <div class="stat_prot_title">Запросы</div>
                                <div class="stat_prot_elem">10%</div>
                            </div>
                            <div class="stat_prot">
                                <div class="stat_prot_title">Лайк / Дизлайк</div>
                                <div class="stat_prot_elem">10 / 90</div>
                            </div>
                        </div>
                        <div class="stat-items-down">
                            <div class="">Лайки - Дизлайки</div>
                            <div class="progress_bar">
                                <progress class="amount-progress" value="90" max="100">70 %</progress>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="row">
                <div class="col">
                    <div class="stat-item">
                        <div class="stat-items-up">
                            <div class="stat_prot">
                                <div class="stat_prot_title">Качество</div>
                                <div class="stat_prot_elem">10%</div>
                            </div>
                            <div class="stat_prot">
                                <div class="stat_prot_title">Запросы</div>
                                <div class="stat_prot_elem">10%</div>
                            </div>
                            <div class="stat_prot">
                                <div class="stat_prot_title">Лайк / Дизлайк</div>
                                <div class="stat_prot_elem">10 / 90</div>
                            </div>
                        </div>
                        <div class="stat-items-down">
                            <div class="">Лайки - Дизлайки</div>
                            <div class="progress_bar">
                                <progress class="amount-progress" value="90" max="100">70 %</progress>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col">
                    <div class="stat-item">
                        <div class="stat-items-up">
                            <div class="stat_prot">
                                <div class="stat_prot_title">Качество</div>
                                <div class="stat_prot_elem">10%</div>
                            </div>
                            <div class="stat_prot">
                                <div class="stat_prot_title">Запросы</div>
                                <div class="stat_prot_elem">10%</div>
                            </div>
                            <div class="stat_prot">
                                <div class="stat_prot_title">Лайк / Дизлайк</div>
                                <div class="stat_prot_elem">10 / 90</div>
                            </div>
                        </div>
                        <div class="stat-items-down">
                            <div class="">Лайки - Дизлайки</div>
                            <div class="progress_bar">
                                <progress class="amount-progress" value="90" max="100">70 %</progress>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col">
                    <div class="stat-item">
                        <div class="stat-items-up">
                            <div class="stat_prot">
                                <div class="stat_prot_title">Качество</div>
                                <div class="stat_prot_elem">10%</div>
                            </div>
                            <div class="stat_prot">
                                <div class="stat_prot_title">Запросы</div>
                                <div class="stat_prot_elem">10%</div>
                            </div>
                            <div class="stat_prot">
                                <div class="stat_prot_title">Лайк / Дизлайк</div>
                                <div class="stat_prot_elem">10 / 90</div>
                            </div>
                        </div>
                        <div class="stat-items-down">
                            <div class="">Лайки - Дизлайки</div>
                            <div class="progress_bar">
                                <progress class="amount-progress" value="90" max="100">70 %</progress>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="row">
                <div class="col">
                    <div class="stat-item">
                        <div class="stat-items-up">
                            <div class="stat_prot">
                                <div class="stat_prot_title">Качество</div>
                                <div class="stat_prot_elem">10%</div>
                            </div>
                            <div class="stat_prot">
                                <div class="stat_prot_title">Запросы</div>
                                <div class="stat_prot_elem">10%</div>
                            </div>
                            <div class="stat_prot">
                                <div class="stat_prot_title">Лайк / Дизлайк</div>
                                <div class="stat_prot_elem">10 / 90</div>
                            </div>
                        </div>
                        <div class="stat-items-down">
                            <div class="">Лайки - Дизлайки</div>
                            <div class="progress_bar">
                                <progress class="amount-progress" value="90" max="100">70 %</progress>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col">
                    <div class="stat-item">
                        <div class="stat-items-up">
                            <div class="stat_prot">
                                <div class="stat_prot_title">Качество</div>
                                <div class="stat_prot_elem">10%</div>
                            </div>
                            <div class="stat_prot">
                                <div class="stat_prot_title">Запросы</div>
                                <div class="stat_prot_elem">10%</div>
                            </div>
                            <div class="stat_prot">
                                <div class="stat_prot_title">Лайк / Дизлайк</div>
                                <div class="stat_prot_elem">10 / 90</div>
                            </div>
                        </div>
                        <div class="stat-items-down">
                            <div class="">Лайки - Дизлайки</div>
                            <div class="progress_bar">
                                <progress class="amount-progress" value="90" max="100">70 %</progress>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col">
                    <div class="stat-item">
                        <div class="stat-items-up">
                            <div class="stat_prot">
                                <div class="stat_prot_title">Качество</div>
                                <div class="stat_prot_elem">10%</div>
                            </div>
                            <div class="stat_prot">
                                <div class="stat_prot_title">Запросы</div>
                                <div class="stat_prot_elem">10%</div>
                            </div>
                            <div class="stat_prot">
                                <div class="stat_prot_title">Лайк / Дизлайк</div>
                                <div class="stat_prot_elem">10 / 90</div>
                            </div>
                        </div>
                        <div class="stat-items-down">
                            <div class="">Лайки - Дизлайки</div>
                            <div class="progress_bar">
                                <progress class="amount-progress" value="90" max="100">70 %</progress>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="row">
                <div class="col">
                    <div class="stat-item">
                        <div class="stat-items-up">
                            <div class="stat_prot">
                                <div class="stat_prot_title">Качество</div>
                                <div class="stat_prot_elem">10%</div>
                            </div>
                            <div class="stat_prot">
                                <div class="stat_prot_title">Запросы</div>
                                <div class="stat_prot_elem">10%</div>
                            </div>
                            <div class="stat_prot">
                                <div class="stat_prot_title">Лайк / Дизлайк</div>
                                <div class="stat_prot_elem">10 / 90</div>
                            </div>
                        </div>
                        <div class="stat-items-down">
                            <div class="">Лайки - Дизлайки</div>
                            <div class="progress_bar">
                                <progress class="amount-progress" value="90" max="100">70 %</progress>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col">
                    <div class="stat-item">
                        <div class="stat-items-up">
                            <div class="stat_prot">
                                <div class="stat_prot_title">Качество</div>
                                <div class="stat_prot_elem">10%</div>
                            </div>
                            <div class="stat_prot">
                                <div class="stat_prot_title">Запросы</div>
                                <div class="stat_prot_elem">10%</div>
                            </div>
                            <div class="stat_prot">
                                <div class="stat_prot_title">Лайк / Дизлайк</div>
                                <div class="stat_prot_elem">10 / 90</div>
                            </div>
                        </div>
                        <div class="stat-items-down">
                            <div class="">Лайки - Дизлайки</div>
                            <div class="progress_bar">
                                <progress class="amount-progress" value="90" max="100">70 %</progress>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col">
                    <div class="stat-item">
                        <div class="stat-items-up">
                            <div class="stat_prot">
                                <div class="stat_prot_title">Качество</div>
                                <div class="stat_prot_elem">10%</div>
                            </div>
                            <div class="stat_prot">
                                <div class="stat_prot_title">Запросы</div>
                                <div class="stat_prot_elem">10%</div>
                            </div>
                            <div class="stat_prot">
                                <div class="stat_prot_title">Лайк / Дизлайк</div>
                                <div class="stat_prot_elem">10 / 90</div>
                            </div>
                        </div>
                        <div class="stat-items-down">
                            <div class="">Лайки - Дизлайки</div>
                            <div class="progress_bar">
                                <progress class="amount-progress" value="90" max="100">70 %</progress>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="row">
                <div class="col">
                    <div class="stat-item">
                        <div class="stat-items-up">
                            <div class="stat_prot">
                                <div class="stat_prot_title">Качество</div>
                                <div class="stat_prot_elem">10%</div>
                            </div>
                            <div class="stat_prot">
                                <div class="stat_prot_title">Запросы</div>
                                <div class="stat_prot_elem">10%</div>
                            </div>
                            <div class="stat_prot">
                                <div class="stat_prot_title">Лайк / Дизлайк</div>
                                <div class="stat_prot_elem">10 / 90</div>
                            </div>
                        </div>
                        <div class="stat-items-down">
                            <div class="">Лайки - Дизлайки</div>
                            <div class="progress_bar">
                                <progress class="amount-progress" value="90" max="100">70 %</progress>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col">
                    <div class="stat-item">
                        <div class="stat-items-up">
                            <div class="stat_prot">
                                <div class="stat_prot_title">Качество</div>
                                <div class="stat_prot_elem">10%</div>
                            </div>
                            <div class="stat_prot">
                                <div class="stat_prot_title">Запросы</div>
                                <div class="stat_prot_elem">10%</div>
                            </div>
                            <div class="stat_prot">
                                <div class="stat_prot_title">Лайк / Дизлайк</div>
                                <div class="stat_prot_elem">10 / 90</div>
                            </div>
                        </div>
                        <div class="stat-items-down">
                            <div class="">Лайки - Дизлайки</div>
                            <div class="progress_bar">
                                <progress class="amount-progress" value="90" max="100">70 %</progress>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col">
                    <div class="stat-item">
                        <div class="stat-items-up">
                            <div class="stat_prot">
                                <div class="stat_prot_title">Качество</div>
                                <div class="stat_prot_elem">10%</div>
                            </div>
                            <div class="stat_prot">
                                <div class="stat_prot_title">Запросы</div>
                                <div class="stat_prot_elem">10%</div>
                            </div>
                            <div class="stat_prot">
                                <div class="stat_prot_title">Лайк / Дизлайк</div>
                                <div class="stat_prot_elem">10 / 90</div>
                            </div>
                        </div>
                        <div class="stat-items-down">
                            <div class="">Лайки - Дизлайки</div>
                            <div class="progress_bar">
                                <progress class="amount-progress" value="90" max="100">70 %</progress>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="row">
                <div class="col">
                    <div class="stat-item">
                        <div class="stat-items-up">
                            <div class="stat_prot">
                                <div class="stat_prot_title">Качество</div>
                                <div class="stat_prot_elem">10%</div>
                            </div>
                            <div class="stat_prot">
                                <div class="stat_prot_title">Запросы</div>
                                <div class="stat_prot_elem">10%</div>
                            </div>
                            <div class="stat_prot">
                                <div class="stat_prot_title">Лайк / Дизлайк</div>
                                <div class="stat_prot_elem">10 / 90</div>
                            </div>
                        </div>
                        <div class="stat-items-down">
                            <div class="">Лайки - Дизлайки</div>
                            <div class="progress_bar">
                                <progress class="amount-progress" value="90" max="100">70 %</progress>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col">
                    <div class="stat-item">
                        <div class="stat-items-up">
                            <div class="stat_prot">
                                <div class="stat_prot_title">Качество</div>
                                <div class="stat_prot_elem">10%</div>
                            </div>
                            <div class="stat_prot">
                                <div class="stat_prot_title">Запросы</div>
                                <div class="stat_prot_elem">10%</div>
                            </div>
                            <div class="stat_prot">
                                <div class="stat_prot_title">Лайк / Дизлайк</div>
                                <div class="stat_prot_elem">10 / 90</div>
                            </div>
                        </div>
                        <div class="stat-items-down">
                            <div class="">Лайки - Дизлайки</div>
                            <div class="progress_bar">
                                <progress class="amount-progress" value="90" max="100">70 %</progress>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col">
                    <div class="stat-item">
                        <div class="stat-items-up">
                            <div class="stat_prot">
                                <div class="stat_prot_title">Качество</div>
                                <div class="stat_prot_elem">10%</div>
                            </div>
                            <div class="stat_prot">
                                <div class="stat_prot_title">Запросы</div>
                                <div class="stat_prot_elem">10%</div>
                            </div>
                            <div class="stat_prot">
                                <div class="stat_prot_title">Лайк / Дизлайк</div>
                                <div class="stat_prot_elem">10 / 90</div>
                            </div>
                        </div>
                        <div class="stat-items-down">
                            <div class="">Лайки - Дизлайки</div>
                            <div class="progress_bar">
                                <progress class="amount-progress" value="90" max="100">70 %</progress>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="row">
                <div class="col">
                    <div class="stat-item">
                        <div class="stat-items-up">
                            <div class="stat_prot">
                                <div class="stat_prot_title">Качество</div>
                                <div class="stat_prot_elem">10%</div>
                            </div>
                            <div class="stat_prot">
                                <div class="stat_prot_title">Запросы</div>
                                <div class="stat_prot_elem">10%</div>
                            </div>
                            <div class="stat_prot">
                                <div class="stat_prot_title">Лайк / Дизлайк</div>
                                <div class="stat_prot_elem">10 / 90</div>
                            </div>
                        </div>
                        <div class="stat-items-down">
                            <div class="">Лайки - Дизлайки</div>
                            <div class="progress_bar">
                                <progress class="amount-progress" value="90" max="100">70 %</progress>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col">
                    <div class="stat-item">
                        <div class="stat-items-up">
                            <div class="stat_prot">
                                <div class="stat_prot_title">Качество</div>
                                <div class="stat_prot_elem">10%</div>
                            </div>
                            <div class="stat_prot">
                                <div class="stat_prot_title">Запросы</div>
                                <div class="stat_prot_elem">10%</div>
                            </div>
                            <div class="stat_prot">
                                <div class="stat_prot_title">Лайк / Дизлайк</div>
                                <div class="stat_prot_elem">10 / 90</div>
                            </div>
                        </div>
                        <div class="stat-items-down">
                            <div class="">Лайки - Дизлайки</div>
                            <div class="progress_bar">
                                <progress class="amount-progress" value="90" max="100">70 %</progress>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col">
                    <div class="stat-item">
                        <div class="stat-items-up">
                            <div class="stat_prot">
                                <div class="stat_prot_title">Качество</div>
                                <div class="stat_prot_elem">10%</div>
                            </div>
                            <div class="stat_prot">
                                <div class="stat_prot_title">Запросы</div>
                                <div class="stat_prot_elem">10%</div>
                            </div>
                            <div class="stat_prot">
                                <div class="stat_prot_title">Лайк / Дизлайк</div>
                                <div class="stat_prot_elem">10 / 90</div>
                            </div>
                        </div>
                        <div class="stat-items-down">
                            <div class="">Лайки - Дизлайки</div>
                            <div class="progress_bar">
                                <progress class="amount-progress" value="90" max="100">70 %</progress>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="row">
                <div class="col">
                    <div class="graf-items">
                        <div class="grag-title">График ---</div>
                        <div class="grafic"><canvas id="myChart1"></canvas></div>
                    </div>
                </div>
                <div class="col">
                    <div class="graf-items">
                        <div class="grag-title">График ---</div>
                        <div class="grafic"><canvas id="myChart2"></canvas></div>
                    </div>
                </div>
            </div>
        </div>
    </div>

</template>

<style scoped>
body {
    background-color: rgb(141, 11, 11);
    padding: 110px;
}
.grag-title{
    display: flex;
    justify-content: center;
}
.row {
    margin-top: 20px;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
}

.stat-item, .graf-items {
    display: flex;
    flex-direction: column;
    box-shadow: 0px 0px 50px 16px rgba(0, 0, 0, 0.1);

}

.stat-items-down {
    margin: 15px;
}

.stat_prot {
    display: flex;
    flex-direction: column;
    width: 33%;
}

.stat-items-up {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    margin: 15px;
}

.progress_bar {
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
}

progress {
    border-radius: 2px;
    width: 100%;
    height: 30px;
    box-shadow: 1px 1px 4px rgba(0, 0, 0, 0.2);
}

progress::-webkit-progress-bar {
    border-radius: 2px;
    background-color: rgb(231, 236, 240);
}

progress::-webkit-progress-value {
    background-color: rgb(7, 107, 236);
    border-radius: 2px;
    box-shadow: 1px 1px 4px rgba(0, 0, 0, 0.2);
}

progress::-moz-progress-bar {
    /* style rules */
}

.progress_bar {
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
}
</style>
