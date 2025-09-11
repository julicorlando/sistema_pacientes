<?php
/**
 * Evolution Delete Handler
 * Sistema de Pacientes - PHP Migration
 */

require_once 'includes/auth.php';
require_once 'includes/functions.php';

// Require login
$auth->requireLogin();

// Check if this is a POST request
if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    redirect('dashboard.php', 'Método inválido.', 'error');
}

// Get parameters
$evolution_id = intval($_POST['evolution_id'] ?? 0);
$patient_id = intval($_POST['patient_id'] ?? 0);
$user = $auth->getUser();
$csrf_token = $_POST['csrf_token'] ?? '';

// Verify CSRF token
if (!verifyCSRFToken($csrf_token)) {
    redirect('dashboard.php', 'Token de segurança inválido.', 'error');
}

if (!$evolution_id || !$patient_id) {
    redirect('dashboard.php', 'Parâmetros inválidos.', 'error');
}

$db = getDB();

// Verify evolution belongs to a patient of the current user
$sql = "SELECT e.id, p.nome 
        FROM evolucoes e 
        JOIN pacientes p ON e.paciente_id = p.id 
        WHERE e.id = ? AND e.paciente_id = ? AND p.usuario_id = ?";

$evolucao = $db->fetch($sql, [$evolution_id, $patient_id, $user['id']]);

if (!$evolucao) {
    redirect('dashboard.php', 'Evolução não encontrada.', 'error');
}

// Delete evolution from database
try {
    $sql = "DELETE FROM evolucoes WHERE id = ?";
    $db->execute($sql, [$evolution_id]);
    
    redirect("evolution_list.php?patient_id=$patient_id", 'Evolução excluída com sucesso!');
    
} catch (Exception $e) {
    redirect("evolution_list.php?patient_id=$patient_id", 'Erro ao excluir evolução: ' . $e->getMessage(), 'error');
}
?>