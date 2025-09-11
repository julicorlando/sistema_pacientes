<?php
/**
 * Patient Dashboard - List Patients
 * Sistema de Pacientes - PHP Migration
 */

require_once 'includes/auth.php';
require_once 'includes/functions.php';

// Require login
$auth->requireLogin();

// Get current user
$user = $auth->getUser();

// Get patients for current user
$db = getDB();
$sql = "SELECT id, nome, telefone, email, cpf, created_at 
        FROM pacientes 
        WHERE usuario_id = ? 
        ORDER BY nome ASC";

$pacientes = $db->fetchAll($sql, [$user['id']]);

// Set page variables
$page_title = 'Lista de Pacientes';
$css_files = ['listar.css'];
$show_nav = true;

// Include header
require_once 'includes/header.php';
?>

<header>
    <h1>Lista de Pacientes</h1>
    <!-- Navigation is handled by includes/header.php -->
</header>

<!-- Campo de busca -->
<div class="search-container">
    <input type="text" id="search" placeholder="Buscar paciente..." class="search-input">
</div>

<section class="table-container">
    <?php if (!empty($pacientes)): ?>
        <?php foreach ($pacientes as $paciente): ?>
            <ul class="paciente-item">
                <li class="paciente-nome"><?php echo htmlspecialchars($paciente['nome']); ?></li>
                <li><a href="patient_details.php?id=<?php echo $paciente['id']; ?>">Ver detalhes</a></li>
                <li><a href="patient_delete.php?id=<?php echo $paciente['id']; ?>">Excluir</a></li>
                <li><a href="patient_edit.php?id=<?php echo $paciente['id']; ?>">Editar</a></li>
                <li><a href="payment_add.php?patient_id=<?php echo $paciente['id']; ?>" class="btn btn-primary">Adicionar Pagamento</a></li>
            </ul>
        <?php endforeach; ?>
    <?php else: ?>
        <p class="empty-message">Nenhum paciente cadastrado.</p>
    <?php endif; ?>
</section>

<!-- Script jQuery para busca dinâmica -->
<script>
    $(document).ready(function() {
        $('#search').on('input', function() {
            var value = $(this).val().toLowerCase();
            $('.paciente-item').filter(function() {
                $(this).toggle($(this).text().toLowerCase().includes(value));
            });
        });
    });
</script>

<?php require_once 'includes/footer.php'; ?>