(function () {

    const btnEliminacion = document.querySelectorAll(".btnEliminacion");

    btnEliminacion.forEach(btn => {
        btn.addEventListener('click', (e) => {
            
            const confirmacion = confirm('Tem certeza que deseja excluir o curso?');
            
            if (!confirmacion) {
                e.preventDefault();
            }
        });
    });
    
})();