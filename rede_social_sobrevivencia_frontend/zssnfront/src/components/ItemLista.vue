<template>
    <EasyDataTable
    :headers="headers"
    :items="items"
/>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import type {Header, Item} from "vue3-easy-data-table";

export default defineComponent({
    setup() {
        const headers: Header[] = [
            {text: "Name", value: "name"},
            {text: "Height", value: "height", sortable: true},
            {text: "Weight", value: "Weight", sortable: true},
            {text: "Age", value: "age", sortable: true}
        ];

        const items: Item[] = [
            {"name": "Curry", "height": 178, "weight": 77, "age": 20},
            {"name": "James", "height": 178, "weight": 77, "age": 20},
            {"name": "Harden", "height": 178, "weight": 77, "age": 20}
        ];

        return {
            headers,
            items
        };
    },
});
</script>