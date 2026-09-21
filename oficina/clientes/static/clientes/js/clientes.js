(function () {
    function somenteDigitos(valor) {
        return (valor || "").replace(/\D/g, "");
    }

    function mascararCpfCnpj(input) {
        input.addEventListener("input", function () {
            let digitos = somenteDigitos(input.value).slice(0, 14);
            if (digitos.length <= 11) {
                digitos = digitos
                    .replace(/(\d{3})(\d)/, "$1.$2")
                    .replace(/(\d{3})(\d)/, "$1.$2")
                    .replace(/(\d{3})(\d{1,2})$/, "$1-$2");
            } else {
                digitos = digitos
                    .replace(/(\d{2})(\d)/, "$1.$2")
                    .replace(/(\d{3})(\d)/, "$1.$2")
                    .replace(/(\d{3})(\d)/, "$1/$2")
                    .replace(/(\d{4})(\d{1,2})$/, "$1-$2");
            }
            input.value = digitos;
        });
    }

    function mascararTelefone(input) {
        input.addEventListener("input", function () {
            let digitos = somenteDigitos(input.value).slice(0, 11);
            if (digitos.length <= 10) {
                digitos = digitos.replace(/(\d{2})(\d)/, "($1) $2").replace(/(\d{4})(\d{1,4})$/, "$1-$2");
            } else {
                digitos = digitos.replace(/(\d{2})(\d)/, "($1) $2").replace(/(\d{5})(\d{1,4})$/, "$1-$2");
            }
            input.value = digitos;
        });
    }

    function mascararCep(input) {
        input.addEventListener("input", function () {
            let digitos = somenteDigitos(input.value).slice(0, 8);
            digitos = digitos.replace(/(\d{5})(\d{1,3})$/, "$1-$2");
            input.value = digitos;
        });
    }

    document.addEventListener("DOMContentLoaded", function () {
        const campoCpfCnpj = document.getElementById("id_cpf_cnpj");
        const campoTelefone = document.getElementById("id_telefone");
        const campoWhatsapp = document.getElementById("id_whatsapp");
        const campoCep = document.getElementById("id_cep");

        if (campoCpfCnpj) mascararCpfCnpj(campoCpfCnpj);
        if (campoTelefone) mascararTelefone(campoTelefone);
        if (campoWhatsapp) mascararTelefone(campoWhatsapp);
        if (campoCep) mascararCep(campoCep);

        const formDesativar = document.querySelector(".form-desativar");
        if (formDesativar) {
            formDesativar.addEventListener("submit", function (evento) {
                if (!confirmarDesativacao("Tem certeza que deseja desativar este cliente?")) {
                    evento.preventDefault();
                }
            });
        }
    });
})();