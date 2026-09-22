(function () {
    function mascararPlaca(input) {
        input.addEventListener("input", function () {
            input.value = input.value.toUpperCase().replace(/[^A-Z0-9]/g, "").slice(0, 7);
        });
    }

    function bloquearNegativo(input) {
        input.addEventListener("input", function () {
            if (input.value !== "" && parseInt(input.value, 10) < 0) {
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

    document.addEventListener("DOMContentLoaded", function () {
        const campoPlaca = document.getElementById("id_placa");
        const campoModelo = document.getElementById("id_modelo");
        const campoCapacidade = document.getElementById("id_capacidade_maxima");

        if (campoPlaca) {
            mascararPlaca(campoPlaca);
            validarObrigatorio(campoPlaca, "A placa é obrigatória.");
        }
        if (campoModelo) validarObrigatorio(campoModelo, "O modelo é obrigatório.");
        if (campoCapacidade) bloquearNegativo(campoCapacidade);

        const formDesativar = document.querySelector(".form-desativar");
        if (formDesativar) {
            formDesativar.addEventListener("submit", function (evento) {
                if (!confirmarDesativacao("Tem certeza que deseja desativar este veículo?")) {
                    evento.preventDefault();
                }
            });
        }
    });
})();