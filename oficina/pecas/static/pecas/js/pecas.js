(function () {
    function bloquearNegativo(input) {
        input.addEventListener("input", function () {
            if (input.value !== "" && parseFloat(input.value) < 0) {
                input.value = 0;
            }
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
        const campoCodigo = document.getElementById("id_codigo");
        const campoNome = document.getElementById("id_nome");
        const campoEstoqueAtual = document.getElementById("id_estoque_atual");
        const campoEstoqueMinimo = document.getElementById("id_estoque_minimo");
        const campoPrecoCusto = document.getElementById("id_preco_custo");
        const campoPrecoVenda = document.getElementById("id_preco_venda");

        if (campoCodigo) validarObrigatorio(campoCodigo, "O código é obrigatório.");
        if (campoNome) validarObrigatorio(campoNome, "O nome é obrigatório.");

        [campoEstoqueAtual, campoEstoqueMinimo, campoPrecoCusto, campoPrecoVenda].forEach(function (campo) {
            if (campo) bloquearNegativo(campo);
        });

        [campoPrecoCusto, campoPrecoVenda].forEach(function (campo) {
            if (campo) formatarMoedaAoSair(campo);
        });

        const formDesativar = document.querySelector(".form-desativar");
        if (formDesativar) {
            formDesativar.addEventListener("submit", function (evento) {
                if (!confirmarDesativacao("Tem certeza que deseja desativar esta peça?")) {
                    evento.preventDefault();
                }
            });
        }
    });
})();