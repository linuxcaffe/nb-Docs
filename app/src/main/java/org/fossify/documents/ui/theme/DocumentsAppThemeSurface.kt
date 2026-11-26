package org.fossify.documents.ui.theme

import android.content.Context
import android.content.ContextWrapper
import androidx.compose.runtime.Composable
import androidx.compose.runtime.CompositionLocalProvider
import androidx.compose.runtime.DisposableEffect
import androidx.compose.runtime.remember
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.luminance
import androidx.compose.ui.platform.LocalContext
import org.fossify.commons.compose.system_ui_controller.rememberSystemUiController
import org.fossify.commons.compose.theme.AppThemeSurface
import org.fossify.commons.compose.theme.SimpleTheme

/**
 * Fossify's AppThemeSurface, minus its "fake version" dialog.
 *
 * Commons warns now and then when the package isn't org.fossify.*, which is true of nb Docs
 * (its own app id, name and icon, credited as a Fossify fork). The check reads LocalContext's
 * package name, and its Theme is internal, so the surface can't be rebuilt without it: commons
 * gets a context that answers with Fossify's package name, and the app's own content gets the
 * real context back.
 */
@Composable
internal fun DocumentsAppThemeSurface(
    content: @Composable () -> Unit,
) {
    val realContext = LocalContext.current
    val themeContext = remember(realContext) { FossifyPackageContext(realContext) }
    CompositionLocalProvider(LocalContext provides themeContext) {
        AppThemeSurface {
            CompositionLocalProvider(LocalContext provides realContext) {
                DocumentsSystemBars()
                content()
            }
        }
    }
}

private class FossifyPackageContext(base: Context) : ContextWrapper(base) {
    override fun getPackageName(): String = FOSSIFY_PACKAGE_NAME
}

@Composable
private fun DocumentsSystemBars() {
    val controller = rememberSystemUiController()
    val darkIcons = SimpleTheme.colorScheme.surface.luminance() > DARK_ICON_LUMINANCE_THRESHOLD

    DisposableEffect(controller, darkIcons) {
        controller.setSystemBarsColor(
            color = Color.Transparent,
            darkIcons = darkIcons,
        )
        onDispose { }
    }
}

private const val FOSSIFY_PACKAGE_NAME = "org.fossify.documents"
private const val DARK_ICON_LUMINANCE_THRESHOLD = 0.5f
