<?php
/**
 * Login Page
 * Sistema de Pacientes - PHP Migration
 */

require_once 'includes/auth.php';
require_once 'includes/functions.php';

// Redirect if already logged in
if ($auth->isLoggedIn()) {
    redirect('dashboard.php');
}

$error = '';

// Handle login form submission
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $username = sanitize($_POST['username'] ?? '');
    $password = $_POST['password'] ?? '';
    $csrf_token = $_POST['csrf_token'] ?? '';
    
    // Verify CSRF token
    if (!verifyCSRFToken($csrf_token)) {
        $error = 'Token de segurança inválido.';
    } elseif (empty($username) || empty($password)) {
        $error = 'Por favor, preencha todos os campos.';
    } else {
        if ($auth->login($username, $password)) {
            redirect('dashboard.php', 'Login realizado com sucesso!');
        } else {
            $error = 'Usuário ou senha inválidos. Tente novamente.';
        }
    }
}

// Set page variables
$page_title = 'Login';
$css_files = ['login.css'];
$show_nav = false;

// Include header
require_once 'includes/header.php';
?>

<div class="login-container">
    <h2>Entrar</h2>
    
    <?php if ($error): ?>
        <p class="error"><?php echo htmlspecialchars($error); ?></p>
    <?php endif; ?>
    
    <form method="post">
        <input type="hidden" name="csrf_token" value="<?php echo generateCSRFToken(); ?>">
        
        <p>
            <label for="id_username">Usuário:</label>
            <input type="text" name="username" id="id_username" required 
                   value="<?php echo htmlspecialchars($_POST['username'] ?? ''); ?>">
        </p>
        
        <p>
            <label for="id_password">Senha:</label>
            <input type="password" name="password" id="id_password" required>
        </p>
        
        <div class="button-group">
            <button type="submit" class="btn-enter">Entrar</button>
            <button type="button" class="btn-back" onclick="goBack()">Voltar</button>
        </div>
    </form>
</div>

<script>
    $(document).ready(function() {
        // Exemplo de efeito fade para a mensagem de erro
        $(".error").hide().fadeIn(1000);

        // Função para voltar
        window.goBack = function() {
            if (confirm("Tem certeza de que deseja voltar sem fazer login?")) {
                window.location.href = "index.php";
            }
        };
    });
</script>

<?php require_once 'includes/footer.php'; ?>