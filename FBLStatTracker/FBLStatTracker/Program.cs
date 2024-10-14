using FBLStatTracker.Components;
using ElectronNET.API;
using ElectronNET.API.Entities;
using ThisBlazorApp = FBLStatTracker.Components.App; // Clarifies ambiguity with ElectronNET.API.App

namespace FBLStatTracker {
    public class Program {
        public static void Main(string[] args) {
            var builder = WebApplication.CreateBuilder(args);

            // Add electron
            builder.WebHost.UseElectron(args);

            // Add services to the container.
            builder.Services.AddRazorComponents()
                .AddInteractiveServerComponents();

            var app = builder.Build();

            // Configure the HTTP request pipeline.
            if (!app.Environment.IsDevelopment()) {

                app.UseExceptionHandler("/Error");
                // The default HSTS value is 30 days. You may want to change this for production scenarios, see https://aka.ms/aspnetcore-hsts.
                app.UseHsts();
            }

            app.UseHttpsRedirection();

            app.UseStaticFiles();
            app.UseAntiforgery();

            app.MapRazorComponents<ThisBlazorApp>()
                .AddInteractiveServerRenderMode();

            // Dynamically create Electron app state
            if(HybridSupport.IsElectronActive) {
                Task.Run(async () => {
                    // Controls for window
                    var opt = new BrowserWindowOptions {
                        Show = false,
                        Frame = false,
                        // Mac traffic lights for the Mac homies
                        TitleBarStyle = OperatingSystem.IsMacOS() ? TitleBarStyle.hiddenInset : TitleBarStyle.hidden
                    };

                    // window init
                    var window = await Electron.WindowManager.CreateWindowAsync();

                    // events
                    window.OnReadyToShow += () =>
                    {
                        window.Maximize();
                        window.Show();
                    };
                    window.OnClosed += () => Electron.App.Quit();
                });
            }

            app.Run();
        }
    }
}
