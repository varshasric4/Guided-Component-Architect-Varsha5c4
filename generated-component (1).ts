import { Component } from '@angular/core';

@Component({
  selector: 'app-login-card',
  template: `
    <div style="display: flex; justify-content: center; align-items: center; height: 100vh; background: rgba(255, 255, 255, 0.1); backdrop-filter: blur(10px);">
      <div style="background: rgba(255, 255, 255, 0.2); border-radius: 8px; padding: 32px; box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
        <h2 style="font-family: Inter; text-align: center;">Login</h2>
        <form>
          <div style="margin-bottom: 16px;">
            <input type="text" placeholder="Username" style="width: 100%; padding: 12px; border-radius: 8px; border: 2px solid #0ea5e9;"/>
          </div>
          <div style="margin-bottom: 16px;">
            <input type="password" placeholder="Password" style="width: 100%; padding: 12px; border-radius: 8px; border: 2px solid #0ea5e9;"/>
          </div>
          <button type="submit" style="width: 100%; padding: 12px; background-color: #6366f1; color: white; border: none; border-radius: 8px; cursor: pointer;">Login</button>
        </form>
      </div>
    </div>
  `,
  styles: []
})
export class LoginCardComponent {}