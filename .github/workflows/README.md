# CI/CD Workflows para sensingpy

Este directorio contiene los workflows de GitHub Actions para automatizar el desarrollo, testing, documentación y release del paquete sensingpy.

## 📋 Workflows Disponibles

### 1. **CI - Tests and Quality** (`ci.yml`)
**Trigger:** Push/PR a `main` o `develop`

**Funcionalidad:**
- ✅ Ejecuta tests en múltiples OS (Ubuntu, Windows, macOS)
- ✅ Prueba con Python 3.11 y 3.12
- ✅ Genera reportes de cobertura
- ✅ Verifica formato de código (Black, isort)
- ✅ Linting con Ruff
- ✅ Type checking con mypy

### 2. **Build and Deploy Documentation** (`docs.yml`)
**Trigger:** Push a `main` que modifique código o docs

**Funcionalidad:**
- 📚 Construye documentación Sphinx automáticamente
- 🌐 Publica en GitHub Pages
- 📦 Genera artefactos de documentación
- 🔄 Actualización automática en cada push

**URL de documentación:** `https://aouei.github.io/sensingpy`

### 3. **Auto Version and Tag** (`auto-tag.yml`)
**Trigger:** 
- Push a `main` con mensaje que contenga `[release]`
- Dispatch manual con bump type (major/minor/patch)

**Funcionalidad:**
- 🏷️ Extrae versión de `pyproject.toml`
- 🔖 Crea tag git automáticamente
- 📝 Genera GitHub Release
- 🔗 Enlaza documentación en release notes

### 4. **Release to PyPI** (`publish_to_pypi.yml`)
**Trigger:** Push de tags `v*.*.*`

**Funcionalidad:**
- 📦 Construye distribuciones (wheel y sdist)
- 🚀 Publica en PyPI automáticamente
- 🔐 Usa trusted publishing (no necesita tokens)

## 🚀 Flujo de Trabajo Completo

### Para una nueva versión:

1. **Actualizar versión en `pyproject.toml`:**
   ```toml
   version = "1.3.0"  # Cambiar versión
   ```

2. **Commit con mensaje especial:**
   ```bash
   git add pyproject.toml
   git commit -m "[release] Version 1.3.0 - Added new features"
   git push origin main
   ```

3. **Automatización se encarga de:**
   - ✅ Ejecutar tests
   - ✅ Construir documentación
   - ✅ Crear tag `v1.3.0`
   - ✅ Publicar docs en GitHub Pages
   - ✅ Crear GitHub Release
   - ✅ Publicar en PyPI

## 📝 Configuración Requerida

### Secrets de GitHub:
- `PYPI_API_TOKEN`: Token de PyPI para publicación automática

### Configuración de GitHub Pages:
1. Ir a Settings → Pages
2. Source: Deploy from a branch
3. Branch: `gh-pages` / `/ (root)`

### Configuración de PyPI Trusted Publishing:
1. Ir a PyPI → Manage → Publishing
2. Añadir GitHub Actions workflow
3. Configurar: `Aouei/sensingpy` con workflow `publish_to_pypi.yml`

## 🛠️ Uso Manual

### Trigger documentación manualmente:
```bash
gh workflow run docs.yml
```

### Crear tag manualmente:
```bash
gh workflow run auto-tag.yml -f bump_type=minor
```

### Publicar a PyPI manualmente:
```bash
git tag v1.3.0
git push origin v1.3.0
```

## 📊 Status Badges

Añade estos badges a tu README.md:

```markdown
![CI](https://github.com/Aouei/sensingpy/workflows/CI%20-%20Tests%20and%20Quality/badge.svg)
![Docs](https://github.com/Aouei/sensingpy/workflows/Build%20and%20Deploy%20Documentation/badge.svg)
![PyPI](https://img.shields.io/pypi/v/sensingpy)
![Python](https://img.shields.io/pypi/pyversions/sensingpy)
```

## 🔄 Actualización de Workflows

Para modificar los workflows:
1. Editar archivos `.yml` en `.github/workflows/`
2. Commit y push
3. Los cambios se aplican automáticamente

## ⚠️ Troubleshooting

### Documentación no se publica:
- Verificar que GitHub Pages esté habilitado
- Revisar permisos de Actions en Settings → Actions → General

### Tag ya existe:
- El workflow verifica duplicados automáticamente
- Incrementar versión en `pyproject.toml`

### Tests fallan:
- Revisar logs en Actions tab
- Ejecutar tests localmente: `pytest tests/`
