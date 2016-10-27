import { RouterModule, Routes } from '@angular/router';

import { HomeComponent } from './home/home.component';
import { InputComponent } from './input/input.component';
import { OutputComponent } from './output/output.component';

const routes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'input', component: InputComponent},
  { path: 'output', component: OutputComponent}
];

export const routing = RouterModule.forRoot(routes);
