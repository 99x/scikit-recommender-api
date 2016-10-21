import { TestBed } from '@angular/core/testing';

import { InputComponent } from './input.component';

describe('Input Component', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({declarations: [InputComponent]});
  });

  it('should ...', () => {
    const fixture = TestBed.createComponent(InputComponent);
    fixture.detectChanges();
    expect(fixture.nativeElement.children[0].textContent).toContain('Input Works!');
  });

});
