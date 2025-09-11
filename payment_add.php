<?php
/**
 * Add Payment Form
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

$errors = [];

// Handle form submission
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $csrf_token = $_POST['csrf_token'] ?? '';
    $valor = sanitize($_POST['valor'] ?? '');
    $forma_pagamento = sanitize($_POST['forma_pagamento'] ?? '');
    
    // Verify CSRF token
    if (!verifyCSRFToken($csrf_token)) {
        $errors[] = 'Token de segurança inválido.';
    }
    
    // Validate required fields
    if (empty($valor)) {
        $errors[] = 'Valor é obrigatório.';
    } elseif (!is_numeric($valor) || floatval($valor) <= 0) {
        $errors[] = 'Valor deve ser um número positivo.';
    }
    
    if (empty($forma_pagamento)) {
        $errors[] = 'Forma de pagamento é obrigatória.';
    }
    
    // If no errors, insert payment
    if (empty($errors)) {
        try {
            $sql = "INSERT INTO pagamentos (paciente_id, valor, forma_pagamento) VALUES (?, ?, ?)";
            $db->execute($sql, [$patient_id, floatval($valor), $forma_pagamento]);
            
            redirect("patient_details.php?id=$patient_id", 'Pagamento adicionado com sucesso!');
            
        } catch (Exception $e) {
            $errors[] = 'Erro ao adicionar pagamento: ' . $e->getMessage();
        }
    }
}

// Get select options
$options = getSelectOptions();

// Set page variables
$page_title = 'Adicionar Pagamento - ' . $paciente['nome'];
$css_files = ['pagamento.css'];
$show_nav = true;

// Include header
require_once 'includes/header.php';
?>

<!-- Título da Página -->
<h1>Adicionar Pagamento</h1>
<h2>Paciente: <?php echo htmlspecialchars($paciente['nome']); ?></h2>

<!-- Erro Messages -->
<?php if (!empty($errors)): ?>
    <div class="error-messages">
        <?php foreach ($errors as $error): ?>
            <p class="error"><?php echo htmlspecialchars($error); ?></p>
        <?php endforeach; ?>
    </div>
<?php endif; ?>

<!-- Formulário de Pagamento -->
<main>
    <form method="post" class="form-pagamento">
        <input type="hidden" name="csrf_token" value="<?php echo generateCSRFToken(); ?>">
        
        <p>
            <label for="id_valor">Valor (R$):</label>
            <input type="number" name="valor" id="id_valor" required min="0.01" step="0.01"
                   value="<?php echo htmlspecialchars($_POST['valor'] ?? ''); ?>"
                   placeholder="0,00">
        </p>
        
        <p>
            <label for="id_forma_pagamento">Forma de pagamento:</label>
            <?php echo generateSelect('forma_pagamento', $options['forma_pagamento'], $_POST['forma_pagamento'] ?? '', 'id="id_forma_pagamento" required'); ?>
        </p>
        
        <div class="form-buttons">
            <button type="submit" class="btn-primary">Salvar Pagamento</button>
            <a href="patient_details.php?id=<?php echo $patient_id; ?>" class="btn-secondary">Cancelar</a>
        </div>
    </form>
</main>

<style>
.form-pagamento {
    max-width: 500px;
    margin: 40px auto;
    padding: 30px;
    background: #ffffff;
    border-radius: 10px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
}

.form-pagamento p {
    margin-bottom: 20px;
}

.form-pagamento label {
    display: block;
    margin-bottom: 5px;
    font-weight: bold;
    color: #333;
}

.form-pagamento input,
.form-pagamento select {
    width: 100%;
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 5px;
    font-size: 16px;
    box-sizing: border-box;
}

.form-pagamento input:focus,
.form-pagamento select:focus {
    outline: none;
    border-color: #8cacb4;
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
    max-width: 500px;
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