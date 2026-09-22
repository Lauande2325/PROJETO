(function () {
    function bloquearNegativo(input) {
        input.addEventListener("input", function () {
            if (input.value !== "" && parseFloat(input.value) < 0) {
                input.value = 0;
            }
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

    function formatarMoedaAoSair(input) {
        input.addEventListener("blur", function () {
            const valor = parseFloat(input.value);
            if (!isNaN(valor)) {
                input.value = valor.toFixed(2);
            }
        });
    }

    document.addEventListener("DOMContentLoaded", function () {
        const campoNome = document.getElementById("id_nome");
        const campoDuracao = document.getElementById("id_duracao_estimada_minutos");
        const campoPreco = document.getElementById("id_preco");

        if (campoNome) validarObrigatorio(campoNome, "O nome é obrigatório.");
        if (campoDuracao) bloquearNegativo(campoDuracao);
        if (campoPreco) {
            bloquearNegativo(campoPreco);
            formatarMoedaAoSair(campoPreco);
        }

        const formDesativar = document.querySelector(".form-desativar");
        if (formDesativar) {
            formDesativar.addEventListener("submit", function (evento) {
                if (!confirmarDesativacao("Tem certeza que deseja desativar este serviço?")) {
                    evento.preventDefault();
                }
            });
        }
    });
})();