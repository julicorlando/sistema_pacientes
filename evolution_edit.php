<?php
/**
 * Edit Evolution Page
 * Sistema de Pacientes - PHP Migration
 */

require_once 'includes/auth.php';
require_once 'includes/functions.php';

// Require login
$auth->requireLogin();

// Get evolution ID
$evolution_id = intval($_GET['id'] ?? 0);
$user = $auth->getUser();

if (!$evolution_id) {
    redirect('dashboard.php', 'Evolução não encontrada.', 'error');
}

$db = getDB();

// Get evolution details (ensure patient belongs to current user)
$sql = "SELECT e.*, p.nome as paciente_nome, p.id as paciente_id
        FROM evolucoes e 
        JOIN pacientes p ON e.paciente_id = p.id 
        WHERE e.id = ? AND p.usuario_id = ?";

$evolucao = $db->fetch($sql, [$evolution_id, $user['id']]);

if (!$evolucao) {
    redirect('dashboard.php', 'Evolução não encontrada.', 'error');
}

$errors = [];

// Handle form submission
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $csrf_token = $_POST['csrf_token'] ?? '';
    $conteudo = sanitize($_POST['conteudo'] ?? '');
    
    // Verify CSRF token
    if (!verifyCSRFToken($csrf_token)) {
        $errors[] = 'Token de segurança inválido.';
    }
    
    // Validate content
    if (empty($conteudo)) {
        $errors[] = 'Conteúdo da evolução é obrigatório.';
    }
    
    // If no errors, update evolution
    if (empty($errors)) {
        try {
            $sql = "UPDATE evolucoes SET conteudo = ? WHERE id = ?";
            $db->execute($sql, [$conteudo, $evolution_id]);
            
            redirect("evolution_list.php?patient_id={$evolucao['paciente_id']}", 'Evolução atualizada com sucesso!');
            
        } catch (Exception $e) {
            $errors[] = 'Erro ao atualizar evolução: ' . $e->getMessage();
        }
    }
    
    // If errors, use POST data for form values
    if (!empty($errors)) {
        $evolucao['conteudo'] = $conteudo;
    }
}

// Set page variables
$page_title = 'Editar Evolução - ' . $evolucao['paciente_nome'];
$css_files = ['evolucao.css'];
$show_nav = true;

// Include header
require_once 'includes/header.php';
?>

<!-- Título da Página -->
<h1>Editar Evolução</h1>
<h2>Paciente: <?php echo htmlspecialchars($evolucao['paciente_nome']); ?></h2>
<p class="evolucao-data">
    <strong>Data da Evolução:</strong> <?php echo formatDate($evolucao['data'], 'd/m/Y H:i'); ?>
</p>

<!-- Erro Messages -->
<?php if (!empty($errors)): ?>
    <div class="error-messages">
        <?php foreach ($errors as $error): ?>
            <p class="error"><?php echo htmlspecialchars($error); ?></p>
        <?php endforeach; ?>
    </div>
<?php endif; ?>

<!-- Formulário de Edição -->
<main>
    <form method="post" class="form-evolucao">
        <input type="hidden" name="csrf_token" value="<?php echo generateCSRFToken(); ?>">
        
        <p>
            <label for="id_conteudo">Conteúdo da Evolução:</label>
            <textarea name="conteudo" id="id_conteudo" required 
                      placeholder="Escreva a evolução do paciente aqui..."><?php echo htmlspecialchars($evolucao['conteudo']); ?></textarea>
        </p>
        
        <div class="form-buttons">
            <button type="submit" class="btn-primary">Atualizar Evolução</button>
            <a href="evolution_list.php?patient_id=<?php echo $evolucao['paciente_id']; ?>" class="btn-secondary">Cancelar</a>
        </div>
    </form>
</main>

<style>
.form-evolucao {
    max-width: 800px;
    margin: 40px auto;
    padding: 30px;
    background: #ffffff;
    border-radius: 10px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
}

.form-evolucao p {
    margin-bottom: 20px;
}

.form-evolucao label {
    display: block;
    margin-bottom: 10px;
    font-weight: bold;
    color: #333;
}

.form-evolucao textarea {
    width: 100%;
    min-height: 200px;
    padding: 15px;
    border: 1px solid #ddd;
    border-radius: 5px;
    font-family: Arial, sans-serif;
    font-size: 14px;
    line-height: 1.6;
    resize: vertical;
    box-sizing: border-box;
}

.form-evolucao textarea:focus {
    outline: none;
    border-color: #8cacb4;
    box-shadow: 0 0 5px rgba(140, 172, 180, 0.3);
}

.form-buttons {
    display: flex;
    gap: 15px;
    justify-content: center;
    margin-top: 30px;
}

.btn-primary,
.btn-secondary {
    padding: 12px 24px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-weight: bold;
    text-decoration: none;
    display: inline-block;
    text-align: center;
    transition: background-color 0.3s;
}

.btn-primary {
    background-color: #8cacb4;
    color: white;
}

.btn-primary:hover {
    background-color: #7a9ba4;
}

.btn-secondary {
    background-color: #757575;
    color: white;
}

.btn-secondary:hover {
    background-color: #616161;
}

.error-messages {
    max-width: 800px;
    margin: 20px auto;
}

.error {
    background-color: #ffebee;
    color: #d32f2f;
    padding: 10px;
    border-radius: 5px;
    margin-bottom: 10px;
    border: 1px solid #f44336;
}

.evolucao-data {
    text-align: center;
    color: #666;
    font-style: italic;
    margin-bottom: 30px;
}

h1, h2 {
    text-align: center;
    color: #8cacb4;
}

h2 {
    font-size: 1.3em;
    margin-bottom: 10px;
}
</style>

<?php require_once 'includes/footer.php'; ?>