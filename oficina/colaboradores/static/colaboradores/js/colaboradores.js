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
        const campoEmail = document.getElementById("id_email");
        const campoCpf = document.getElementById("id_cpf");
        const campoDepartamento = document.getElementById("id_departamento");

        if (campoNome) validarObrigatorio(campoNome, "O nome é obrigatório.");
        if (campoEmail) validarObrigatorio(campoEmail, "O e-mail é obrigatório.");
        if (campoDepartamento) validarObrigatorio(campoDepartamento, "O departamento é obrigatório.");
        if (campoCpf) {
            mascararCpf(campoCpf);
            validarObrigatorio(campoCpf, "O CPF é obrigatório.");
        }

        const formDesativar = document.querySelector(".form-desativar");
        if (formDesativar) {
            formDesativar.addEventListener("submit", function (evento) {
                if (!confirmarDesativacao("Tem certeza que deseja desativar este colaborador?")) {
                    evento.preventDefault();
                }
            });
        }
    });
})();