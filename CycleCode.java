import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.time.format.DateTimeParseException;
import java.time.DayOfWeek;
import java.util.*;

public class CycleCode {

    public static String cycleCode(String date) {
        Map<String, String> dayId = new HashMap<>();
        dayId.put("FRIDAY", "01");
        dayId.put("MONDAY", "02");
        dayId.put("TUESDAY", "03");
        dayId.put("WEDNESDAY", "04");
        dayId.put("THURSDAY", "05");

        try {
            LocalDate datetimeDate = LocalDate.parse(date, DateTimeFormatter.ofPattern("yyyy-MM-dd"));
            DayOfWeek day = datetimeDate.getDayOfWeek();
            int weekNum = datetimeDate.get(java.time.temporal.WeekFields.ISO.weekOfWeekBasedYear());
            if (day==DayOfWeek.SATURDAY || day==DayOfWeek.SUNDAY) {
                return date + " is not a weekday";
            }
            if (day == DayOfWeek.FRIDAY) {
                weekNum += 1;
            }
            if (weekNum==53) {
                weekNum=1;
            }
            String weekNumStr = (weekNum < 10) ? "0" + weekNum : String.valueOf(weekNum);
            int year = datetimeDate.getYear();
            if (datetimeDate.getMonthValue()==12 && weekNumStr.equals("01")) {
                return String.format("%d%s%s", year+1, weekNumStr, dayId.get(day.toString()));
            }
            else {
                return String.format("%d%s%s", year, weekNumStr, dayId.get(day.toString()));
            }
        } catch (DateTimeParseException | NullPointerException e) {
            return "Failed for " + date;
        }
    }

    public static void main(String[] args) {
        // Example dates
        String[] dates = {"2025-12-25"};
        for (String date: dates) System.out.println(cycleCode(date));
    }
}
