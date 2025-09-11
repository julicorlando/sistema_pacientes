<?php
/**
 * Common Header and Navigation
 * Sistema de Pacientes - PHP Migration
 */

require_once __DIR__ . '/auth.php';
require_once __DIR__ . '/functions.php';

// Update user activity
$auth->updateActivity();

// Get flash message if any
$flash = getFlashMessage();
?>

<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title><?php echo isset($page_title) ? $page_title . ' - ' . APP_NAME : APP_NAME; ?></title>
    
    <!-- CSS Files -->
    <?php if (isset($css_files)): ?>
        <?php foreach ($css_files as $css_file): ?>
            <link rel="stylesheet" type="text/css" href="static/css/<?php echo $css_file; ?>">
        <?php endforeach; ?>
    <?php else: ?>
        <link rel="stylesheet" type="text/css" href="static/css/styles.css">
    <?php endif; ?>
    
    <!-- jQuery -->
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    
    <!-- Additional JS Files -->
    <?php if (isset($js_files)): ?>
        <?php foreach ($js_files as $js_file): ?>
            <script src="static/js/<?php echo $js_file; ?>" defer></script>
        <?php endforeach; ?>
    <?php endif; ?>
</head>
<body class="<?php echo isset($body_class) ? $body_class : ''; ?>">

<?php if (isset($show_nav) && $show_nav !== false): ?>
    <nav>
        <ul class="nav-links">
            <li><a href="index.php">Página Inicial</a></li>
            <?php if ($auth->isLoggedIn()): ?>
                <li><a href="dashboard.php">Acessar Sistema</a></li>
                <li><a href="patient_add.php">Cadastrar Paciente</a></li>
                <li><a href="register.php">Cadastrar Novo Usuário</a></li>
                <li>
                    <form action="logout.php" method="post" style="display: inline;">
                        <input type="hidden" name="csrf_token" value="<?php echo generateCSRFToken(); ?>">
                        <button class="btn-logout" type="submit">Sair</button>
                    </form>
                </li>
            <?php else: ?>
                <li><a href="login.php">Acesso Restrito</a></li>
            <?php endif; ?>
        </ul>
    </nav>
<?php endif; ?>

<?php if ($flash): ?>
    <div class="alert alert-<?php echo $flash['type']; ?>">
        <?php echo htmlspecialchars($flash['message']); ?>
    </div>
    <script>
        // Auto-hide flash messages after 5 seconds
        setTimeout(function() {
            $('.alert').fadeOut();
        }, 5000);
    </script>
<?php endif; ?>

<div class="content">