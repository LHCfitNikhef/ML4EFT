	  if (pt(p(0,3)) + pt(p(0,4)) .lt. 150.0d0) then
            if (r2min(5,6) .gt. 3.0d0) then
                  dummy_cuts=.false.
            endif
      endif

      if (pt(p(0,3)) + pt(p(0,4)) .lt. 200.0d0 .and. pt(p(0,3)) + pt(p(0,4)) .ge. 150.0d0) then
            if (r2min(5,6) .gt. 1.8d0) then
                  dummy_cuts=.false.
            endif
      end if

      if (pt(p(0,3)) + pt(p(0,4)) .ge. 200.0d0) then
            if (r2min(5,6) .gt. 1.2d0) then
                  dummy_cuts=.false.
            endif
      endif