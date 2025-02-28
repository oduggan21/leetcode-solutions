
        zipped_list = sorted(zip(position, speed), reverse = True)
        stack = []
        count = 0

        for pos, speed in (zipped_list):

            time_to_destination = (target - pos) / speed
 
            if not stack or time_to_destination > stack[-1]:
                stack.append(time_to_destination)
            
        
        return len(stack)
        
