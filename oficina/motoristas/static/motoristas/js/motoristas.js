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

    function mascararCnh(input) {
        input.addEventListener("input", function () {
            input.value = somenteDigitos(input.value).slice(0, 11);
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
        const campoCnh = document.getElementById("id_cnh");
        const campoCpf = document.getElementById("id_cpf");

        if (campoNome) validarObrigatorio(campoNome, "O nome é obrigatório.");
        if (campoCnh) {
            mascararCnh(campoCnh);
            validarObrigatorio(campoCnh, "A CNH é obrigatória.");
        }
        if (campoCpf) {
            mascararCpf(campoCpf);
            validarObrigatorio(campoCpf, "O CPF é obrigatório.");
        }

        const formDesativar = document.querySelector(".form-desativar");
        if (formDesativar) {
            formDesativar.addEventListener("submit", function (evento) {
                if (!confirmarDesativacao("Tem certeza que deseja desativar este motorista?")) {
                    evento.preventDefault();
                }
            });
        }
    });
})();