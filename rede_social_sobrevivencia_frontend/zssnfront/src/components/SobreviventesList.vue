<template>
    <div class="content">
        <h1>Sobreviventes App</h1>

        <div class="add_form">
            <form v-on:submit.prevent="submitSobrevivente">
                <input type="text" class="form-control" placeholder="Nome" v-model="nome" />
                <input type="text" class="form-control" placeholder="Idade" v-model="idade" />
                <input type="text" class="form-control" placeholder="Sexo" v-model="sexo" />
                <input type="text" class="form-control" placeholder="latitude" v-model="latitude" />
                <input type="text" class="form-control" placeholder="longitude" v-model="longitude" />
                <button type="submit" class="btn btn-primary">
                    {{ isEditing ? "Edit Sobrevivente" : "Add Sobrevivente" }}
                </button>
            </form>
        </div>

        <div class="list">
            <table class="list_content">
                <tr>
                    <th>Nome</th>
                    <th>Idade</th>
                    <th>Sexo</th>
                    <th>Latitude</th>
                    <th>Longitude</th>
                    <th>Infectado</th>
                    <th>Item</th>
                    <th>Botão</th>
                </tr>
                <tr v-for="sobrevivente in sobreviventes" :key="sobrevivente.id">
                    <td>{{ sobrevivente.nome }}</td>
                    <td>{{ sobrevivente.idade }}</td>
                    <td>{{ sobrevivente.sexo }}</td>
                    <td>{{ sobrevivente.latitude }}</td>
                    <td>{{ sobrevivente.longitude }}</td>
                    <input class="checkbox" type="checkbox" v-model="sobrevivente.infectado" />
                    <template v-if="sobrevivente.items.length">
                        <td>
                            <div v-for="item in sobrevivente.items">{{ item.nome }}:{{ item.pontos }} pontos</div>
                        </td>
                    </template>
                    <td v-else>Sem Item</td>
                    <td class="list_buttons">
                        <button @click="editSobrevivente(sobrevivente)">Editar</button>
                        <button @click="deleteSobrevivente(sobrevivente)">Deletar</button>
                    </td>
                </tr>
            </table>
        </div>
    </div>
</template>


<script>
export default {
    data() {
        return {
            sobreviventes: [],
            nome: "",
            idade: "",
            sexo: "",
            latitude: "",
            longitude: "",
            infectado: "",
            id: "",
            isEditing: false,
        };
    },
    methods: {
        async getSobrevivente() {
            try {
                await this.$http.get(`http://127.0.0.1:8000/api/sobreviventes/`).then(response => {
                    this.sobreviventes = response.data;
                });
            } catch (error) {
                console.log(error);
            }
        },
        async submitSobrevivente() {
            try {
                if (!this.isEditing) {
                    await this.$http.post(`http://127.0.0.1:8000/api/sobreviventes/`, {
                        nome: this.nome,
                        idade: this.idade,
                        sexo: this.sexo,
                        latitude: this.latitude,
                        longitude: this.longitude,
                        infectado: false,
                    })
                        .then((response) => {
                            this.sobreviventes.push(response.data);
                            this.nome = "";
                            this.idade = "";
                            this.sexo = "";
                            this.latitude = "";
                            this.longitude = "";
                            this.infectado = "";
                        });
                } else {
                    await this.$http.put(`http://127.0.0.1:8000/api/sobreviventes/${this.id}/`, {
                        nome: this.nome,
                        idade: this.idade,
                        sexo: this.sexo,
                        latitude: this.latitude,
                        longitude: this.longitude,
                        infectado: false,
                    })
                        .then(response => {
                            let objIndex = this.sobreviventes.findIndex((s) => s.id === this.id);
                            let tmp = this.sobreviventes;
                            tmp[objIndex] = response.data;
                            this.sobreviventes = tmp;
                            this.idade = "",
                                this.sexo = "",
                                this.latitude = "",
                                this.longitude = "",
                                this.infectado = "",
                                this.isEditing = false,
                                this.getSobrevivente();
                        });
                }
            } catch (error) {
                console.log(error);
            }
        },
        async editSobrevivente(sobrevivente) {
            try {
                this.isEditing = true;
                this.nome = sobrevivente.nome;
                this.idade = sobrevivente.idade;
                this.sexo = sobrevivente.sexo;
                this.latitude = sobrevivente.latitude;
                this.longitude = sobrevivente.longitude;
                this.infectado = sobrevivente.infectado;
                this.id = sobrevivente.id;
            } catch (error) {
                console.log(error);
            }
        },
        async deleteSobrevivente(sobrevivente) {
            if (!confirm("Você tem certeza?")) {
                return;
            }
            await this.$http.delete(`http://127.0.0.1:8000/api/sobreviventes/${sobrevivente.id}/`);
            await this.getSobrevivente();
        },
    },
    created() {
        this.getSobrevivente();
    },
}
</script>

<style scoped>
table {
    font-family: arial, sans-serif;
    border-collapse: collapse;
    width: 100%;
    text-align:center;
}
td,
th {
    border: 1px solid #dddddd;
    text-align: center;
    padding: 6px;
}
.checkbox {
    cursor:pointer;
    padding: 10px;
    width: 80px;
    margin-top: 50px;
    display: inherit;
}

tr:nth-child(even) {
    background-color: #cf5454;
}

table {
    border: 1px solid black;
    table-layout: fixed;
    width: 100px;
}

th,
td {
    border: 1px solid black;
    width: 200px;
    overflow: hidden;
}
</style>