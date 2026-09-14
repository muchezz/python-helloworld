<?php
$path = parse_url($_SERVER['REQUEST_URI'] ?? '/', PHP_URL_PATH);
if ($path === '/hello') {
    echo 'Hello from plain PHP on NjiraCloud';
} else {
    echo 'NjiraCloud plain PHP fixture';
}
