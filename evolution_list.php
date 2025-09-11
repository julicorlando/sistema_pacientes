<?php
/**
 * Evolution List Page
 * Sistema de Pacientes - PHP Migration
 */

require_once 'includes/auth.php';
require_once 'includes/functions.php';

// Require login
$auth->requireLogin();

// Get patient ID
$patient_id = intval($_GET['patient_id'] ?? 0);
$user = $auth->getUser();

if (!$patient_id) {
    redirect('dashboard.php', 'Paciente não encontrado.', 'error');
}

$db = getDB();

// Get patient details (ensure it belongs to current user)
$sql = "SELECT id, nome FROM pacientes WHERE id = ? AND usuario_id = ?";
$paciente = $db->fetch($sql, [$patient_id, $user['id']]);

if (!$paciente) {
    redirect('dashboard.php', 'Paciente não encontrado.', 'error');
}

// Get patient evolutions
$sql = "SELECT * FROM evolucoes WHERE paciente_id = ? ORDER BY data DESC";
$evolucoes = $db->fetchAll($sql, [$patient_id]);

// Set page variables
$page_title = 'Evoluções - ' . $paciente['nome'];
$css_files = ['evolucao.css'];
$show_nav = true;

// Include header
require_once 'includes/header.php';
?>

<!-- Título da Página -->
<h1>Evoluções do Paciente</h1>
<h2>Paciente: <?php echo htmlspecialchars($paciente['nome']); ?></h2>

<!-- Navegação -->
<div class="navigation-links">
    <a href="patient_details.php?id=<?php echo $patient_id; ?>" class="btn">Voltar aos Detalhes</a>
    <a href="dashboard.php" class="btn">Lista de Pacientes</a>
</div>

<!-- Lista de Evoluções -->
<section class="evolucoes-container">
    <?php if (!empty($evolucoes)): ?>
        <?php foreach ($evolucoes as $evolucao): ?>
            <div class="evolucao-item">
                <div class="evolucao-header">
                    <span class="evolucao-data">
                        <strong>Data:</strong> <?php echo formatDate($evolucao['data'], 'd/m/Y H:i'); ?>
                    </span>
                    <div class="evolucao-actions">
                        <a href="evolution_edit.php?id=<?php echo $evolucao['id']; ?>" class="btn btn-small">Editar</a>
                        <form action="evolution_delete.php" method="post" style="display: inline;">
                            <input type="hidden" name="csrf_token" value="<?php echo generateCSRFToken(); ?>">
                            <input type="hidden" name="evolution_id" value="<?php echo $evolucao['id']; ?>">
                            <input type="hidden" name="patient_id" value="<?php echo $patient_id; ?>">
                            <button type="submit" class="btn btn-small btn-danger" 
                                    onclick="return confirm('Tem certeza que deseja excluir esta evolução?');">
                                Excluir
                            </button>
                        </form>
                    </div>
                </div>
                <div class="evolucao-content">
                    <?php echo nl2br(htmlspecialchars($evolucao['conteudo'])); ?>
                </div>
            </div>
        <?php endforeach; ?>
    <?php else: ?>
        <div class="empty-message">
            <p>Nenhuma evolução registrada para este paciente.</p>
        </div>
    <?php endif; ?>
</section>

<!-- Adicionar Nova Evolução -->
<section class="nova-evolucao">
    <h3>Adicionar Nova Evolução</h3>
    <form action="patient_details.php?id=<?php echo $patient_id; ?>" method="post">
        <input type="hidden" name="csrf_token" value="<?php echo generateCSRFToken(); ?>">
        <textarea name="conteudo" placeholder="Escreva a evolução do paciente aqui..." required></textarea>
        <button type="submit" class="btn btn-primary">Salvar Evolução</button>
    </form>
</section>

<style>
.evolucoes-container {
    max-width: 800px;
    margin: 30px auto;
}

.evolucao-item {
    background: #ffffff;
    border: 1px solid #ddd;
    border-radius: 8px;
    margin-bottom: 20px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.evolucao-header {
    background: #f5f5f5;
    padding: 15px;
    border-bottom: 1px solid #ddd;
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
}

.evolucao-data {
    color: #666;
    font-size: 14px;
}

.evolucao-actions {
    display: flex;
    gap: 10px;
}

.evolucao-content {
    padding: 20px;
    line-height: 1.6;
    color: #333;
}

.nova-evolucao {
    max-width: 800px;
    margin: 40px auto;
    background: #ffffff;
    padding: 30px;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.nova-evolucao h3 {
    margin-bottom: 20px;
    color: #8cacb4;
}

.nova-evolucao textarea {
    width: 100%;
    min-height: 120px;
    padding: 15px;
    border: 1px solid #ddd;
    border-radius: 5px;
    font-family: Arial, sans-serif;
    font-size: 14px;
    resize: vertical;
    box-sizing: border-box;
}

.nova-evolucao textarea:focus {
    outline: none;
    border-color: #8cacb4;
}

.navigation-links {
    text-align: center;
    margin: 30px 0;
}

.navigation-links .btn {
    margin: 0 10px;
}

.btn {
    background-color: #8cacb4;
    color: white;
    padding: 10px 20px;
    text-decoration: none;
    border-radius: 5px;
    display: inline-block;
    border: none;
    cursor: pointer;
    font-size: 14px;
    transition: background-color 0.3s;
}

.btn:hover {
    background-color: #7a9ba4;
}

.btn-small {
    padding: 6px 12px;
    font-size: 12px;
}

.btn-primary {
    background-color: #2196f3;
    margin-top: 15px;
}

.btn-primary:hover {
    background-color: #1976d2;
}

.btn-danger {
    background-color: #f44336;
}

.btn-danger:hover {
    background-color: #d32f2f;
}

.empty-message {
    text-align: center;
    padding: 40px;
    color: #666;
    font-style: italic;
}

h1, h2 {
    text-align: center;
    color: #8cacb4;
}

h2 {
    font-size: 1.3em;
    margin-bottom: 30px;
}
</style>

<?php require_once 'includes/footer.php'; ?>