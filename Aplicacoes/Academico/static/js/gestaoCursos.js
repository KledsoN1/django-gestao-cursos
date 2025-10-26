(function () {

    const btnExclusao = document.querySelectorAll(".btnExclusao");

    btnExclusao.forEach(btn => {
        btn.addEventListener('click', (e) => {
                    
            const confirmacao = confirm('Tem certeza que deseja excluir o curso?');
            
            if (!confirmacao) {
                e.preventDefault();
            }
        });
    });
    
})();