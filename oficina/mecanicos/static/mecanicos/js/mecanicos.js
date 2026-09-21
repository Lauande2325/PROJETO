(function () {
    function somenteDigitos(valor) {
        return (valor || "").replace(/\D/g, "");
    }

    function mascararCpf(input) {
        input.addEventListener("input", function () {
            let digitos = somenteDigitos(input.value).slice(0, 11);
            digitos = digitos
                .replace(/(\d{3})(\d)/, "$1.$2")
                .replace(/(\d{3})(\d)/, "$1.$2")
                .replace(/(\d{3})(\d{1,2})$/, "$1-$2");
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

    function validarObrigatorio(input, mensagem) {
        input.addEventListener("blur", function () {
            if (!input.value.trim()) {
                input.setCustomValidity(mensagem);
            } else {
                input.setCustomValidity("");
            }
            input.reportValidity();
        });
    }

    document.addEventListener("DOMContentLoaded", function () {
        const campoNome = document.getElementById("id_nome");
        const campoCpf = document.getElementById("id_cpf");
        const campoTelefone = document.getElementById("id_telefone");
        const campoWhatsapp = document.getElementById("id_whatsapp");

        if (campoNome) validarObrigatorio(campoNome, "O nome é obrigatório.");
        if (campoCpf) mascararCpf(campoCpf);
        if (campoTelefone) mascararTelefone(campoTelefone);
        if (campoWhatsapp) mascararTelefone(campoWhatsapp);

        const formDesativar = document.querySelector(".form-desativar");
        if (formDesativar) {
            formDesativar.addEventListener("submit", function (evento) {
                if (!confirmarDesativacao("Tem certeza que deseja desativar este mecânico?")) {
                    evento.preventDefault();
                }
            });
        }
    });
})();