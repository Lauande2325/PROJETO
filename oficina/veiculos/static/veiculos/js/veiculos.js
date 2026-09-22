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

    document.addEventListener("DOMContentLoaded", function () {
        const campoPlaca = document.getElementById("id_placa");
        const campoQuilometragem = document.getElementById("id_quilometragem");

        if (campoPlaca) mascararPlaca(campoPlaca);
        if (campoQuilometragem) bloquearNegativo(campoQuilometragem);

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