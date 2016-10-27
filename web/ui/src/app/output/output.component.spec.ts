import { TestBed } from '@angular/core/testing';

import { OutputComponent } from './output.component';

describe('Output Component', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({declarations: [OutputComponent]});
  });

  it('should ...', () => {
    const fixture = TestBed.createComponent(OutputComponent);
    fixture.detectChanges();
    expect(fixture.nativeElement.children[0].textContent).toContain('Output works fine!');
  });

});
