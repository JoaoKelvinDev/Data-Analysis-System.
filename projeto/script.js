document.getElementById("csvFile").addEventListener("change", function (e) {
  const file = e.target.files[0];
  if (!file) return;

  Papa.parse(file, {
    header: true,
    skipEmptyLines: true,
    complete: function (results) {
      const alunos = results.data;

      const container = document.getElementById("alunos");
      container.innerHTML = "";

      if (alunos.length === 0) {
        container.innerHTML = "<p class='text-red-400'>Nenhum aluno encontrado.</p>";
        return;
      }

      alunos.forEach((aluno) => {
        const card = document.createElement("div");
        card.className = "bg-gray-800 p-4 rounded shadow-md border border-gray-700";

        card.innerHTML = `
          <p><strong>Nome:</strong> ${aluno.nome}</p>
          <p><strong>Curso:</strong> ${aluno.curso}</p>
          <p><strong>Status:</strong> <span class="${aluno.status.toLowerCase().trim() === 'ativo' ? 'text-green-400' : aluno.status.toLowerCase().trim() === 'cancelado' ? 'text-red-400' : 'text-yellow-400'}">${aluno.status}</span></p>
          <p><strong>Início:</strong> ${aluno.data_inicio}</p>
          <p><strong>Término:</strong> ${aluno.data_fim}</p>
          <p><strong>Frequência:</strong> ${aluno.frequencia}%</p>
        `;

        container.appendChild(card);
      });
    },
  });
});
