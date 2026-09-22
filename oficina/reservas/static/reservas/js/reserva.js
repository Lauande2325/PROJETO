(function () {
    function validarObrigatorio(input, mensagem) {
        if (!input) return;
        input.addEventListener("blur", function () {
            if (!input.value.trim()) {
                input.setCustomValidity(mensagem);
            } else {
                input.setCustomValidity("");
            }
            input.reportValidity();
        });
    }

    function validarHorarios(campoSaida, campoRetorno) {
        if (!campoSaida || !campoRetorno) return;
        function checar() {
            if (campoSaida.value && campoRetorno.value && campoRetorno.value <= campoSaida.value) {
                campoRetorno.setCustomValidity("O horário de retorno deve ser posterior ao horário de saída.");
            } else {
                campoRetorno.setCustomValidity("");
            }
            campoRetorno.reportValidity();
        }
        campoSaida.addEventListener("change", checar);
        campoRetorno.addEventListener("change", checar);
    }

    function validarPassageiros(input) {
        if (!input) return;
        input.addEventListener("input", function () {
            const valor = parseInt(input.value, 10);
            if (!isNaN(valor) && valor > 18) {
                input.value = 18;
            }
            if (input.value !== "" && parseInt(input.value, 10) < 1) {
                input.value = 1;
            }
        });
    }

    document.addEventListener("DOMContentLoaded", function () {
        const campoSetor = document.getElementById("id_setor");
        const campoAtividade = document.getElementById("id_atividade");
        const campoOrigem = document.getElementById("id_origem");
        const campoDestino = document.getElementById("id_destino");
        const campoData = document.getElementById("id_data");
        const campoSaida = document.getElementById("id_horario_saida");
        const campoRetorno = document.getElementById("id_horario_retorno");
        const campoPassageiros = document.getElementById("id_quantidade_passageiros");

        validarObrigatorio(campoSetor, "O setor é obrigatório.");
        validarObrigatorio(campoAtividade, "A atividade é obrigatória.");
        validarObrigatorio(campoOrigem, "A origem é obrigatória.");
        validarObrigatorio(campoDestino, "O destino é obrigatório.");
        validarObrigatorio(campoData, "A data é obrigatória.");
        validarHorarios(campoSaida, campoRetorno);
        validarPassageiros(campoPassageiros);

        const formDesativar = document.querySelector(".form-desativar");
        if (formDesativar) {
            formDesativar.addEventListener("submit", function (evento) {
                if (!confirmarDesativacao("Tem certeza que deseja cancelar esta reserva?")) {
                    evento.preventDefault();
                }
            });
        }
    });
})();