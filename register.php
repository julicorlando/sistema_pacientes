<?php
/**
 * Registration Page
 * Sistema de Pacientes - PHP Migration
 */

require_once 'includes/auth.php';
require_once 'includes/functions.php';

// Require login to access registration (only logged users can create new users)
$auth->requireLogin();

$errors = [];
$success = '';

// Handle registration form submission
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $username = sanitize($_POST['username'] ?? '');
    $email = sanitize($_POST['email'] ?? '');
    $password = $_POST['password1'] ?? '';
    $password_confirm = $_POST['password2'] ?? '';
    $first_name = sanitize($_POST['first_name'] ?? '');
    $last_name = sanitize($_POST['last_name'] ?? '');
    $csrf_token = $_POST['csrf_token'] ?? '';
    
    // Verify CSRF token
    if (!verifyCSRFToken($csrf_token)) {
        $errors[] = 'Token de segurança inválido.';
    }
    
    // Validate required fields
    $required_errors = validateRequired(['username', 'email', 'password1', 'password2'], $_POST);
    $errors = array_merge($errors, $required_errors);
    
    // Validate username
    if (!validateUsername($username)) {
        $errors[] = 'Username deve conter apenas letras, números e _ com 3-150 caracteres.';
    }
    
    // Validate email
    if (!validateEmail($email)) {
        $errors[] = 'Email inválido.';
    }
    
    // Validate password
    if ($password !== $password_confirm) {
        $errors[] = 'As senhas não coincidem.';
    } else {
        $password_errors = validatePassword($password);
        $errors = array_merge($errors, $password_errors);
    }
    
    // If no errors, attempt to register
    if (empty($errors)) {
        $result = $auth->register($username, $email, $password, $first_name, $last_name);
        
        if ($result['success']) {
            $success = $result['message'];
            // Clear form data
            $_POST = [];
        } else {
            $errors[] = $result['message'];
        }
    }
}

// Set page variables
$page_title = 'Cadastro';
$css_files = ['cadastro.css'];
$show_nav = true;

// Include header
require_once 'includes/header.php';
?>

<div class="cadastro-container">
    <h2>Cadastrar Novos Usuários</h2>
    
    <?php if (!empty($errors)): ?>
        <div class="error-messages">
            <?php foreach ($errors as $error): ?>
                <p class="error"><?php echo htmlspecialchars($error); ?></p>
            <?php endforeach; ?>
        </div>
    <?php endif; ?>
    
    <?php if ($success): ?>
        <p class="success"><?php echo htmlspecialchars($success); ?></p>
    <?php endif; ?>
    
    <form method="post">
        <input type="hidden" name="csrf_token" value="<?php echo generateCSRFToken(); ?>">
        
        <p>
            <label for="id_username">Nome de usuário:</label>
            <input type="text" name="username" id="id_username" required
                   value="<?php echo htmlspecialchars($_POST['username'] ?? ''); ?>">
            <small>Obrigatório. 150 caracteres ou menos. Apenas letras, números e @/./+/-/_ .</small>
        </p>
        
        <p>
            <label for="id_email">Email:</label>
            <input type="email" name="email" id="id_email" required
                   value="<?php echo htmlspecialchars($_POST['email'] ?? ''); ?>">
        </p>
        
        <p>
            <label for="id_first_name">Nome:</label>
            <input type="text" name="first_name" id="id_first_name"
                   value="<?php echo htmlspecialchars($_POST['first_name'] ?? ''); ?>">
        </p>
        
        <p>
            <label for="id_last_name">Sobrenome:</label>
            <input type="text" name="last_name" id="id_last_name"
                   value="<?php echo htmlspecialchars($_POST['last_name'] ?? ''); ?>">
        </p>
        
        <p>
            <label for="id_password1">Senha:</label>
            <input type="password" name="password1" id="id_password1" required>
            <small>Sua senha não pode ser muito parecida com suas outras informações pessoais.</small><br>
            <small>Sua senha deve conter pelo menos 8 caracteres.</small><br>
            <small>Sua senha não pode ser uma senha muito comum.</small><br>
            <small>Sua senha não pode ser inteiramente numérica.</small>
        </p>
        
        <p>
            <label for="id_password2">Confirmação de senha:</label>
            <input type="password" name="password2" id="id_password2" required>
            <small>Digite a mesma senha de antes, para verificação.</small>
        </p>
        
        <div class="button-group">
            <button type="submit" class="btn-cadastrar">Cadastrar</button>
            <button type="button" class="btn-voltar" onclick="goBack()">Voltar</button>
        </div>
    </form>
</div>

<script>
    $(document).ready(function() {
        // Função para o botão Voltar
        window.goBack = function() {
            window.location.href = "index.php";
        };

        // Efeito de fade no título
        $("h2").hide().fadeIn(1000);

        // Mensagem de confirmação antes do cadastro
        $(".btn-cadastrar").on("click", function(event) {
            if (!confirm("Tem certeza de que deseja cadastrar este usuário?")) {
                event.preventDefault(); // Evita o envio do formulário se o usuário cancelar
            }
        });
    });
</script>

<?php require_once 'includes/footer.php'; ?>